import pandas as pd
import networkx as nx
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Load the crime data
file_path = 'NYPD_Shooting_Incident_Data__Historic_.csv'
crime_data = pd.read_csv(file_path)

crime_data_cleaned = crime_data[['Latitude', 'Longitude', 'STATISTICAL_MURDER_FLAG']].dropna()


# Assign weights based on crime severity
def calculate_crime_weight(row):
    return 5 if row['STATISTICAL_MURDER_FLAG'] else 1


# Add a weight column
crime_data_cleaned['Weight'] = crime_data_cleaned.apply(calculate_crime_weight, axis=1)

# Limit the number of neighbors to reduce edge complexity
MAX_NEIGHBORS = 5

# Nearest Neighbors algorithm
coordinates = crime_data_cleaned[['Latitude', 'Longitude']].values
nbrs = NearestNeighbors(n_neighbors=MAX_NEIGHBORS, algorithm='ball_tree').fit(coordinates)
distances, indices = nbrs.kneighbors(coordinates)

# Construct the graph with limited edges
G_optimized = nx.Graph()

# Add nodes and edges based on nearest neighbors
for i, neighbors in enumerate(indices):
    for j, neighbor_index in enumerate(neighbors):
        if i != neighbor_index:  # Avoid self-loops
            weight = distances[i][j] * crime_data_cleaned.iloc[i]['Weight']
            G_optimized.add_edge(i, neighbor_index, weight=weight)


# Find the safest route using Dijkstra's algorithm
def find_safest_route(graph, start_node, end_node):
    try:
        path = nx.dijkstra_path(graph, source=start_node, target=end_node, weight='weight')
        total_weight = nx.dijkstra_path_length(graph, source=start_node, target=end_node, weight='weight')
        return path, total_weight
    except nx.NetworkXNoPath:
        return None, float('inf')


# Check if the graph is connected
if nx.is_connected(G_optimized):
    largest_component = G_optimized
else:
    largest_component = G_optimized.subgraph(max(nx.connected_components(G_optimized), key=len))

# Randomly select nodes from the largest connected component
connected_nodes = list(largest_component.nodes)
start_node, end_node = np.random.choice(connected_nodes, 2, replace=False)

# Calculate the safest route
safest_path, safest_path_weight = find_safest_route(largest_component, start_node, end_node)

# Display results
print("Safest Path:", safest_path)
print("Safest Path Weight:", safest_path_weight)

# Assign positions to nodes (latitude and longitude)
for i, (lat, lon) in enumerate(coordinates):
    G_optimized.nodes[i]['pos'] = (lon, lat)


# Visualize the graph and the safest path
def visualize_path(graph, path):
    pos = nx.get_node_attributes(graph, 'pos')  # Retrieve node positions
    plt.figure(figsize=(10, 10))

    # Draw all nodes and edges
    nx.draw(graph, pos, node_size=10, node_color='blue', edge_color='lightgray', alpha=0.5)

    # Highlight the safest path if available
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_size=50, node_color='red')
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Safest Path Visualization")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()


def find_and_display_route():
    try:
        # Retrieve input from the UI
        start_lat = float(start_lat_entry.get())
        start_lon = float(start_lon_entry.get())
        end_lat = float(end_lat_entry.get())
        end_lon = float(end_lon_entry.get())

        # Find the nearest nodes in the graph to the input coordinates
        start_node = nbrs.kneighbors([[start_lat, start_lon]], 1, return_distance=False)[0][0]
        end_node = nbrs.kneighbors([[end_lat, end_lon]], 1, return_distance=False)[0][0]

        # Find the safest route
        path, weight = find_safest_route(largest_component, start_node, end_node)
        if path:
            messagebox.showinfo("Safest Route", f"Safest Path: {path}\nTotal Risk: {weight:.4f}")
            visualize_path(largest_component, path)
        else:
            messagebox.showerror("Error", "No path found between the given locations.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical coordinates.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the Tkinter window
window = tk.Tk()
window.title("Safest Route Finder")
window.geometry("400x300")

tk.Label(window, text="Select Starting Point (Long/Lat):").pack(pady=5)
start_node_var = tk.StringVar(window)
start_node_menu = ttk.Combobox(window, textvariable=start_node_var, state="readonly")
start_node_menu['values'] = list(largest_component.nodes)  # Populate with node IDs
start_node_menu.pack()

tk.Label(window, text="Select End Point (Long/Lat):").pack(pady=5)
end_node_var = tk.StringVar(window)
end_node_menu = ttk.Combobox(window, textvariable=end_node_var, state="readonly")
end_node_menu['values'] = list(largest_component.nodes)  # Populate with node IDs
end_node_menu.pack()


def find_and_display_route_dropdown():
    try:
        start_node = int(start_node_var.get())
        end_node = int(end_node_var.get())

        path, weight = find_safest_route(largest_component, start_node, end_node)
        if path:
            visualize_path(largest_component, path)
        else:
            messagebox.showerror("Error", "No path found between the selected locations.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


calculate_button = tk.Button(window, text="Find Safest Route", command=find_and_display_route_dropdown)
calculate_button.pack(pady=20)

window.mainloop()