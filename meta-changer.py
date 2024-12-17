# Define the input and output file paths
input_file = 'weapons.meta'
output_file = 'weapons_updated.meta'

# Parameters to update with new values
update_values = {
    'MaxHeadShotDistancePlayer': 1000.000000,
    'MinHeadShotDistancePlayer': 0.000000
}

# Read and process the file
with open(input_file, 'r') as file:
    lines = file.readlines()

updated_lines = []
for line in lines:
    # Check if the line contains a parameter to update
    updated = False
    for param, value in update_values.items():
        if param in line:
            # Replace the value in the line
            updated_lines.append(f'        <{param} value="{value:.6f}" />\n')
            updated = True
            break
    if not updated:
        # Keep the line as-is if it doesn't match a parameter
        updated_lines.append(line)

# Save the updated file
with open(output_file, 'w') as file:
    file.writelines(updated_lines)

print(f"Updated file saved as {output_file}")
