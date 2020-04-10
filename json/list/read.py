# coding=gbk
# Base lib import
import json

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
    exit

# Define functions.
def praw(i): # Print raw string.
    print("Printing...\n") # Print tips and add a new line.
    print(i) # Print

def prg(i): # Print the specified index json.
    location = input("Content number: ") # Content number.
    try: # Try to convert location to int instead of string.
        locate = int(location)
    except ValueError: # Cannot convert, because it is not a number. Then errored.
        print("It doesn't a number!") # Friendly error.
        return False # End function
    else: # Converted.
        locate = locate - 1 # The default index is start from 0, instead of 1. So sub 1.
        if locate < 0:
            print("Out of range! Printing last...")
        try: # Check index range.
            p = i[locate] # Save the specified text to p.
        except IndexError: # Index out of range.
            print("Out of range!") # Friendly error.
            return False # End function
        else: # Print
            print(p) # Output

def traverse(i): # Traverse the entire list.
    for t in i:
        print(t + "\n")
    # End

# User
print("What do you want to do with " + filename  + "?")
while True:
    print("1. Print Raw(Not recommended. That will be total mess. And maku sure what are you doing.).")
    print("2. Print text at a specific location.")
    print("3. Traverse(Default, recommended.).")
    o = input("--- ") # User input.
    if o == "1": # Logical check, user selection.
        praw(fs)
    elif o == "2":
        prg(fs)
    else:
        traverse(fs)