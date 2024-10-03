import requests
import csv

# Download the CSV file
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)
csv_content = response.content.decode("utf-8").splitlines()

# Parse the CSV data
data = list(csv.reader(csv_content))

# Calculate the required facts
total_records = len(data) - 1  # Exclude header row

# Find unique boroughs (column 1 is Borough)
boroughs = sorted(set(row[1] for row in data[1:]))  # Skip header row

# Count the number of Brooklyn borough records (case-insensitive)
brooklyn_records = sum(1 for row in data[1:] if row[1].strip().lower() == 'brooklyn')  # Skip header row

# Prepare the output content
output = (
    f"Total Records: {total_records}\n"
    f"Unique Boroughs: {', '.join(boroughs)}\n"
    f"Brooklyn Count: {brooklyn_records}\n"
)

# Save the output to /root/taxi_outputs/taxi_zone_output.txt
with open("/root/taxi_outputs/taxi_zone_output.txt", "w") as f:
    f.write(output)

# Print the output (optional, for confirmation)
print(output)

