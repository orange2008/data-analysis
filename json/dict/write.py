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
        k = input("Key: ")
        v = input("Value: ")
        fs[k] = v
        print("key: " + k + " value: " + v)
        print("Press Ctrl+C to save.")
    except KeyboardInterrupt:
        print("Saving...")
        with open(filename, 'w', encoding="utf-8") as filesystem:
            json.dump(fs, filesystem)
        print("All good!")