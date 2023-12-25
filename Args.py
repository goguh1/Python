# Create an Argparsescript...

# Add arguments for importing any text file and a "verbose" option that prints each line if that option is flagged. 
# Print the total lines from that file at the end of script
# Submit the code and output from running the script with "verbose" and one without "verbose"

import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Read and optionally print lines from a text file.")

# Add argument for importing a text file
parser.add_argument('-f', '--file', type=str, help="Path to the text file")
parser.add_argument("-v", "--verbose", action="store_true", help="Print each line")

# Parse the command line arguments
args = parser.parse_args()

args.file = ''

# Check if the "file" argument is provided
if args.file:
    with open(args.file, 'r') as file:
        lines = file.readlines()

        if args.verbose:
            for line in lines:
                print(line, end="")

        total_lines = len(lines)

        print(f"Total lines in the file: {total_lines}")
else:
    print("Please provide a file using the -f or --file argument.")

#hugog@Hugos-Laptop Python % python3 args.py -f example.txt -v
#1 2 3
#2 
#3Total lines in the file: 3
#hugog@Hugos-Laptop Python % python3 args.py -f example.txt   
#Total lines in the file: 3
