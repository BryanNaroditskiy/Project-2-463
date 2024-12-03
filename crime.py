import pandas as pd
from pandas.tseries.offsets import DateOffset

# Load the dataset from a CSV file
data = pd.read_csv('path_to_your_file.csv')

# Convert the OCCUR_DATE column to datetime format
data['OCCUR_DATE'] = pd.to_datetime(data['OCCUR_DATE'])

# Sort the dataset by the OCCUR_DATE column
data = data.sort_values(by='OCCUR_DATE')

# Count the number of crimes per month
monthly_crimes = data['OCCUR_DATE'].groupby([data.OCCUR_DATE.dt.year, data.OCCUR_DATE.dt.month]).agg('count')

# Print the monthly crime counts
print(monthly_crimes)

# Calculate the average number of crimes per month
average_crimes_per_month = monthly_crimes.mean()

# Predict the next season's crime rate (3 months)
next_season_crime_rate = average_crimes_per_month * 3

print(f'Predicted crimes for the next season: {next_season_crime_rate}')
