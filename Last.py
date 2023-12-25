# Call a commandline tool, using subprocess and shlex. Write a script that calls the "ls" command with "-l" argument on a folder. 
# Print the file and file size of the largest file.​

# command = 'ls -l /some/folder/with/stuff'​

# process = subprocess.Popen(​

#   shlex.split(command),​

#   stdout = subprocess.PIPE,​

#   stderr = subprocess.STDOUT,  # Redirect STDERR to STDOUT, conjoining the two streams​

#   )​

# for line in iter(process.stdout.readline, ''):

import subprocess
import shlex

# Specify the folder path
folder_path = ''

# Build the command
command = f'ls -l {folder_path}'

# Use shlex to split the command into a list of arguments
command_args = shlex.split(command)

# Launch the subprocess
process = subprocess.Popen(
    command_args,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True  # Set text=True to receive output as text (str) instead of bytes
)

# Initialize variables to track the largest file and its size
largest_file = ''
largest_file_size = 0

# Iterate through the output lines
for line in process.stdout:
    # Split the line into columns
    columns = line.split()

    # Check if it's a line with file information
    if len(columns) >= 8:
        # Extract file size and file name
        file_size = int(columns[4])
        file_name = columns[8]

        # Check if the current file is larger than the previous largest file
        if file_size > largest_file_size:
            largest_file_size = file_size
            largest_file = file_name

# Print the result
if largest_file:
    print(f"The largest file in {folder_path} is {largest_file} with a size of {largest_file_size} bytes.")
else:
    print(f"No files found in {folder_path}.")
