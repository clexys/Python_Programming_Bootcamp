# LISTS

# With lists we refer to groups of data with 1 name
# Each item in the list corresponds to a number (index) just like how people have identification numbers
# By default the 1st item in a list has the index 0.

# In Python, lists can grow in size and can contain data of any type
# You can also use many of the same functions with them that you used with strings

rand_list = ["string", 1.234, 28]

# rand_list is the list name
# MUST have []
# Data inside must be separated by a comma

# Create a list with range
one_to_ten = list(range(10))

# List can be combined
rand_list = rand_list + one_to_ten

# Get the 1st item with an index
print(rand_list[0])

# Get the length
print("List Length :", len(rand_list))

# Slice a list to get 1st 3 items
# This is how you get slices with strings too
first3 = rand_list[0:3]

# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
# The number after the * is the amount of time the item will repeat
print(first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")

# PROBLEM

# Generate a random list between 1-9


