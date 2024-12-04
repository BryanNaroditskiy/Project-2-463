# Project-2-463

# Goal of the Project
**Objectives:** The primary objective of this project is to develop a system that analyzes crime data to predict future crime rates and determine the safest paths in a given area to avoid high-risk zones. The project leverages historical crime data to provide predictive insights and to implement a pathfinding algorithm that minimizes exposure to crime-prone areas.

# Significance of the Project
**Meaningfulness and Novelty:** This project is meaningful because it aims to enhance public safety by utilizing data analytics and algorithmic solutions to predict and avoid potential crime scenarios. Its novelty lies in the integration of crime data analysis with Dijkstra's algorithm to identify the safest routes, providing a practical application of academic concepts in a real-world scenario.

# Installation and Instruction to Use
**Installation:**

1. Ensure you have Python installed on your system.

2. Install the required libraries by running:
```bash pip install pandas heapq collections```

**Usage**
1. Place your crime dataset (in CSV format) in the same directory as the script.
2. ``` bash python crime.py```

# Structure of the Code
![image](https://github.com/user-attachments/assets/5d0975a4-4cd0-46ee-acf7-9cdbf56206d9)
The flowchart outlines the steps for predicting the next season's crime rate. It begins by checking for necessary libraries, installing them if they are missing (like pandas, collections, and heapq). Once the libraries are installed, the process involves loading and preprocessing the dataset, extracting the month for sorting, implementing Dijkstra's algorithm to find the safest paths, counting crimes per month, and finally predicting the next season's crime rate based on the data analysis. The flowchart ensures a systematic approach to crime data analysis and safety pathfinding.

# Functionalities and Test Results
**Functionalities:**

* Load and preprocess crime data.

* Sort data using Quicksort.

* Build a graph from the dataset.

* Find the safest path using Dijkstra's algorithm.

* Predict future crime rates.

**Test Results:**

* The dataset was successfully loaded and preprocessed.

* Data was sorted by month using Quicksort.

* A graph was created from the crime data.

* The safest path was determined using Dijkstra's algorithm.

* Future crime rates were predicted for the next season.

# Showcasing the Achievement of Project Goals

**Results:**

* Successfully predicted crime rates for the next season.

* Identified the safest path in the dataset area using Dijkstra's algorithm.

* The results align with the project objectives by enhancing public safety through predictive analytics and algorithmic pathfinding.

# Discussion and Conclusions

**Discussion:**

* Issues: Some limitations include the potential for incomplete or outdated data, which can affect prediction accuracy.

* Limitations: The model assumes a static crime rate, while in reality, crime patterns can change dynamically.

* Application of Course Learning: This project applied concepts of data analysis, sorting algorithms, graph theory, and pathfinding algorithms learned during the course.

**Conclusions:**

The project successfully demonstrated the application of academic concepts to a real-world problem, providing valuable insights into crime data and enhancing public safety through predictive analytics and pathfinding.
