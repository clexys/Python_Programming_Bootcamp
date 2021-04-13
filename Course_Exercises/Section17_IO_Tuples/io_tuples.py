# HERE WE WIL LEARNED HOW TO INTERACT WITH THE FILE SYSTEM AS
# WE ALL WHAT TUPLES ARE

# IT IS A MUST to import the "os" module if we want to interact with files
import os

# The "with" statement, # ensures proper acquisition and release of resources.
# Basically, it closes the file if the program crashes and/or has an error

# open, tells the program it needs to open an existing file. If it doesn't exist,
# it will create it for you, similar to what cat does on bash.

# myfirstfile.txt = we define the name of our file
# mode="w", we define the permissions of the file. In this case, we are
# giving it writing properties.
# NOTE: "w" will overwrite everything on th file.
# To add to the file content, you should use "a"
# encoding="utf-8", we're defining the coding type, in this case Unicode
# as my_file = we're telling the program that the file will assigned to a var

with open("myfirstfile.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Adding some lines to my first file. \nUnderstanding "
                  "how it works.\nAdding more in-lines")

with open("myfirstfile.txt", encoding="utf-8") as my_file:
    print(my_file.read())

# Confirm if the file was actually closed after writing to it
print(my_file.closed)

# Get the file name
print(my_file.name)

# Get the access mode
print(my_file.mode)

# Rename the file
# os.rename("myfirstfile.txt", "myfile2.txt")

# Delete the file
os.remove("myfirstfile.txt")

# Create a Directory
os.mkdir("mydir")
# Change Directory
os.chdir("mydir")

# Verify the Directory we're in
print("Current Directory :", os.getcwd())
# Remove a Directory
# BE VERY CAREFUL!!!!!

# In order to a Dir that is not empty
# Use import shutil
# shutil.rmtree('/folder_name')

# Change back to the Dir
# os.chdir("..")
# Actually removing it.
# os.rmdir("mydir")

# Read One Line at a Time

# You can read one line at a time with readline()

import os

# Open the file
with open("mydata2.txt", encoding="utf-8") as my_file:

    lineNum = 1

    # We'll use a while loop that loops until the data
    # read is empty
    while True:
        line = my_file.readline()

        # line is empty so exit
        if not line:
            break

        print("Line", lineNum, " :", line, end="")

        lineNum += 1