# Tuples

# A Tuple is like a list, but their values can't be changed
# Tuples are used to store multiple items in a single variable.
# Tuples are surrounded with parentheses instead of square brackets

my_tuple = (1, 2, 3, 5, 8)

# Get a value with an index
print("1st Value :", my_tuple[0])

# Get a slice from the 1st index up to but not including
# the 3rd
print(my_tuple[0:3])

# Get the number of items in a Tuple
print("Tuple Length :", len(my_tuple))

# Join or concatenate tuples
more_fibs = my_tuple + (13, 21, 34)

# Check if a value is in a Tuple
print("34 in Tuple :", 34 in more_fibs)

# Iterate through a tuple
for i in more_fibs:
    print(i)

# Convert a List into a Tuple
a_list = [55, 89, 144]
a_tuple = tuple(a_list)

# Convert a Tuple into a List
a_list = list(a_tuple)

# Get max and minimum value
print("Min :", min(a_tuple))
print("Max :", max(a_tuple))