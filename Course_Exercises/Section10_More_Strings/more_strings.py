# Here I'm going deeper into more strings functions
 # MORE STRING FUNCTIONS

# Strings have many methods we can use beyond what I covered last time
rand_string = "   this is an important string   "

# Delete whitespace on left
rand_string = rand_string.lstrip()

# Delete whitespace on right
rand_string = rand_string.rstrip()

# Delete whitespace on right and left
rand_string = rand_string.strip()

# Capitalize the 1st letter
print(rand_string.capitalize())

# Capitalize every letter
print(rand_string.upper())

# lowercase all letters
print(rand_string.lower())

# Turn a list into a string
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Convert a string into a list
rand_string = "this is an important string"
a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

# We can find how many times a string occurs in a string
rand_string = "this is an important string"
print("How many is :", rand_string.count("is"))

# Get an index for a matching string
rand_string = "this is an important string"
print("Where is string :", rand_string.find("string"))

# Replace a string
rand_string = "this is an important string"
print(rand_string.replace("an ", "a kind of "))

# Python Problem

# Acronym generator
# The user will enter a string and then convert it to an
# acronym with uppercase letters like this >>
# Convert to Acronym : Random Access Memory
# RAM

