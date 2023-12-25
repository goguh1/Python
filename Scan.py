# Create a folder on your computer called "week3"
# Create a script that, when run,checks every second indefinitely for a new file in that folder
# If file found,report back to the user:
# 1.File found
# 2.What type of file it is
# 3.When it was put there

# You as the user can introduce whatever file you want to invoke the notification portion of the script (i.e put a text file, image, etc)

import os
from datetime import datetime

# Directory to be scanned
f1 = ''

obj = os.scandir(f1)

# List all files and directories in the specified path
print("Files found in '%s':" % f1)
for entry in obj:
    if entry.is_dir() or entry.is_file():
        name = entry.name
        ctime = datetime.fromtimestamp(entry.stat().st_ctime)
        print(f"{name} - Created on: {ctime.strftime('%Y-%m-%d %H:%M:%S')}")

obj.close()
