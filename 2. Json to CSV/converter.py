import json
import csv

# load the JSON file
with open("input.json", "r") as f:
    data = json.load(f)

# open CSV output
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
