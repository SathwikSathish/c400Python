import requests
import pandas as pd
import os

# Define paths
lookup_csv_path = 'taxi_zone_lookup.csv'  # Save to the current working directory (Jenkins workspace)
output_txt_path = 'taxi_outputs/taxi_zone_output.txt'  # Save output in a subdirectory

# Ensure the output directory exists
os.makedirs('taxi_outputs', exist_ok=True)

# Download the dataset
url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a CSV file
    with open(lookup_csv_path, 'wb') as f:
        f.write(response.content)
    
    # Load the dataset into a DataFrame
    df = pd.read_csv(lookup_csv_path)
    
    # Calculate the required facts
    total_records = len(df)
    unique_boroughs = df['Borough'].unique()
    brooklyn_records = df[df['Borough'] == 'Brooklyn'].shape[0]
    
    # Prepare output facts
    output_facts = (
        f"Total number of records: {total_records}\n"
        f"Unique Boroughs: {', '.join(unique_boroughs)}\n"
        f"Number of records for Brooklyn: {brooklyn_records}\n"
    )
    
    # Save the output facts to a file
    with open(output_txt_path, 'w') as f:
        f.write(output_facts)
else:
    print(f"Failed to download the dataset. Status code: {response.status_code}")
