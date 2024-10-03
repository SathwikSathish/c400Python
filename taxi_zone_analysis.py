import requests
import pandas as pd

# Download the dataset
url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
response = requests.get(url)

# Save the file locally
with open('taxi_zone_lookup.csv', 'wb') as file:
    file.write(response.content)

# Load CSV into pandas DataFrame
df = pd.read_csv('taxi_zone_lookup.csv')

# a. Total number of records sorted in ascending order
sorted_df = df.sort_values(by=df.columns[0])  # Sorting by first column
total_records = sorted_df.shape[0]

# b. Find unique Borough
unique_boroughs = df['Borough'].unique()

# c. Number of records for Brooklyn borough
brooklyn_count = df[df['Borough'] == 'Brooklyn'].shape[0]

# d. Save the facts to output file
with open('/root/taxi_zone_output.txt', 'w') as output_file:
    output_file.write(f'Total records: {total_records}\n')
    output_file.write(f'Unique Boroughs: {unique_boroughs}\n')
    output_file.write(f'Number of records for Brooklyn: {brooklyn_count}\n')
