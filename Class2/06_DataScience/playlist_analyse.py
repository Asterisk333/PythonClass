import json

# Open and load the original JSON file
file_name = "List.json"
with open(file_name, "r", encoding="utf-8") as file:
    data = json.load(file)

# Process the data to add [/] in the beginning of each entry
for key, value_list in data.items():
    data[key] = [f"[/] {entry}" for entry in value_list]

# Write the modified data back to the file
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("File updated successfully.")