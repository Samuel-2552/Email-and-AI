import json

# Specify the path to your JSON file
file_path = "data.json"

# Read the JSON file and parse its content
with open(file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Get the number of items in the JSON object
num_items = len(json_data)

print("Number of items in the JSON object:", num_items)
