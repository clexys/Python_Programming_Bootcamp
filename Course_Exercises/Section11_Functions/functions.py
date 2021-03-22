# FUNCTIONS

def add_number(num_1, num_2):
    return num_1 + num_2
    print("12 + 6 = ", add_number(12, 6))

# Here, the 12 and the 6, are num_1 and num_2.
# That means that when we defined add_number, we told it it would take
# 2 number values, which are the ones we define below when we print the result
# of the operation

''' The below example shows that when a variable is defined inside a function, it
will not be available outside of it. Here, the system will print Tom, regardless of it being defined
as Mark before '''


def change_name(name):
    name = "Mark"
    print(name)

name = "Tom"
change_name(name)
print(name)

def change_name():
    global gbl_name
    gbl_name = "Sammy"

gbl_name = "Salt"
change_name()
print(gbl_name)

# IMPORTANT NOTE
# print will not give me the result of an operation
# return will not give the result of a text
# To get the result of an operation with print I need to first,
# use return for the operation and then print the results

