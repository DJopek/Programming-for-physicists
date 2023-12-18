import os
import json



# Get filepath from user
file = input("Enter the file path: ")

# Read the file to encrypt and its metadata
with open(file, 'rb') as f:
    file_data = f.read()
metadata = os.stat(file)

# Convert binary data to a hex string
hex_data = file_data.hex()

data = {
    'data': hex_data,
    'metadata': metadata,
}

# Convert the dictionary to a JSON string
json_string = json.dumps(str(data))

file_json = input("Enter the JSON file path: ")

# Write the JSON string to a new file
with open(file_json, 'w') as f:
    f.write(json_string)
