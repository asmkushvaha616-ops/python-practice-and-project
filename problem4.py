# WAP to print the contents of directory using the os module .
# Search online for the function which does that
import os

# Specify the path (use '.' for current directory)
path = "/ "

# List all files and directories
contents = os.listdir(path)

# print("Contents of the directory:")
for item in contents:
    print(item)

