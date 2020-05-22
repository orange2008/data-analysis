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

def prk(i): # Print keys.
    for k in i.keys(): # Define a for while, store each key to 'k'.
        print(k) # Print

def prv(i): # Print values.
    for v in i.values(): # Define a for while, store each value to 'v'.
        print(v) # Print

def traverse(i): # Traverse.
    for k,v in i.items(): # Define a for while, store each key to 'k', value to 'v'.
        print(k + "\t" + v) # Print
        
# User
print("What do you want to do with " + filename  + "?")
while True:
    print("1. Print Raw(Not recommended. That will be total mess. And make sure what are you doing.).")
    print("2. Print keys.")
    print("3. Print values.")
    print("4. Print Both Keys and Values(Default, recommended.).")
    o = input("--- ") # User input.
    if o == "1": # Logical check, user selection.
        praw(fs)
    elif o == "2":
        prk(fs)
    elif o == "3":
        prv(fs)
    else:
        traverse(fs)