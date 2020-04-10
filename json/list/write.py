# coding=gbk
# Base lib import
import json
import sys
filename = input("filename: ") # Prompt user to enter filename
if ".json" in filename: # Logical check. Extension, if .json in filename, then don't do anything. If not, add .json
    pass # Don't do anything.
else:
    filename += ".json" # Add .json

try: # Try to open the file.
    with open(filename, 'r', encoding="utf-8") as filesystem: # Open json file. 'r' for Read, 'w' for OverWritten, 'a' for Written. And save object to 'filesystem'.
        fs = json.load(filesystem) # Read json string to 'fs'
except FileNotFoundError: # No such file.
    print("No such file or directory.")
    sys.exit(0)
# Same thing in read.py, we will not use any mark.
while True:
    try:
        t = input("Text(Ctrl+C to quit): ") # User input.
        fs.append(t) # Append to list.
        with open(filename, 'w', encoding="utf-8") as filesystem:
            json.dump(fs, filesystem)
        print("All good!")
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(0)