import requests
import csv


url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)
csv_content = response.content.decode("utf-8").splitlines()


data = list(csv.reader(csv_content))


total_records = len(data) - 1  


boroughs = sorted(set(row[1] for row in data[1:]))


brooklyn_records = sum(1 for row in data if row[1].lower() == 'brooklyn')


output = f"Total Records: {total_records}\\nUnique Boroughs: {boroughs}\\nBrooklyn Count: {brooklyn_records}\\n"
with open("taxi_outputs/taxi_zone_output.txt", "w") as f:
    f.write(output)

print(output)