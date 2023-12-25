# External clients have added spaces throughout the folder names by: internal workflow conflict, user mistake,etc
# We determined the only issue is that there are spaces, but need to confirm which folders
# Write a script that removed all spaces and reports on console which ones needed fixing and which were fine.

import os

f1 = ""

# Read the text file
with open(f1, 'r') as file:
    lines = file.readlines()

# Initialize lists to store folder names that needed fixing and those that were fine
folders_needing_fix = []
folders_okay = []

# Loop through each line
for line in lines:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Split the line into parts using '/'
    parts = line.split('/')
    
    # Remove spaces from each part and join them back with '/'
    new_parts = [part.replace(' ', '') for part in parts]
    new_line = '/'.join(new_parts)
    
    # Check if the modified line is the same as the original line
    if new_line == line:
        folders_okay.append(line)
    else:
        folders_needing_fix.append(line)

# Print results
print("Folders needing fixing:")
for folder in folders_needing_fix:
    print(folder)

print("\nFolders that are okay:")
for folder in folders_okay:
    print(folder)

# Print fixed locations
print("\nFixed locations:")
for folder in folders_needing_fix:
    # Remove spaces from the folder path
    fixed_location = '/'.join([part.replace(' ', '') for part in folder.split('/')])
    print(fixed_location)
