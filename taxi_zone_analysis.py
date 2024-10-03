import requests
import csv

# Download the dataset
url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
response = requests.get(url)

# Save the file locally
with open('taxi_zone_lookup.csv', 'wb') as file:
    file.write(response.content)

# Read the CSV file
with open('taxi_zone_lookup.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header
    records = list(reader)

# a. Total number of records sorted in ascending order
total_records = len(records)

# b. Find unique Borough
unique_boroughs = set(row[2] for row in records)  # Assuming 'Borough' is in the 3rd column (index 2)

# c. Number of records for Brooklyn borough
brooklyn_count = sum(1 for row in records if row[2] == 'Brooklyn')

# d. Save the facts to output file
with open('taxi_zone_output.txt', 'w') as output_file:
    output_file.write(f'Total records: {total_records}\n')
    output_file.write(f'Unique Boroughs: {list(unique_boroughs)}\n')
    output_file.write(f'Number of records for Brooklyn: {brooklyn_count}\n')
