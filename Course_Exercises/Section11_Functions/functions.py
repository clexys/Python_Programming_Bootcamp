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

# FUnction to check if there is a float inside of a string

def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

# is_float >> my function
# str_val >> the argument. Also, is called string value, bcs it represents the number or values that
# will be checked looking for a float
# We can define a variable after we defined a function and throw it inside, like we're going to do with pi

pi = "DOGGIE"
print("Is Pi a float : ", is_float(pi))

# PROBLEM

# Make it print "x + 2 = 6"
# Example print(solve_eq("x + 4 = 9"))

def solv_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)
    return "x = " + str(num_2 - num_1)
print(solv_eq("x + 8 = 5"))

# How in the hell does this work?!
# and How in the hell it can print a result without asking to input a number??!!
# We defined what the "solv_eq" will do
# and we store that into "equation"
# Then, we convert the num_1 and 2 into int.
# Then, we make the operation and output the results with "return"
# It is important that we understand how an equation works.
# To find the value of x we pass the num to the other side
# x + 8 = 5
# x = 5 - 8
# x = -3
# return >> Shows a result on screen. Similar to print
'''Therefore, on return we MUST have the "x = " along with str(num_2 - num_1). 
Otherwise, I will only print the result

1. Why does it have to be str(num_2 - num_1)?? Simple, TypeError: must be str, not int.
It needs to print a string type of character, not an int

Finally, print(solv_eq("x + 8 = 5"))..... We're telling it to print solv_eq
That is the following, 
We passed solv_eq to equation
Then, we defined that equation was equal to x, add, num_1, equal, num_2
IN other words, we declared the structure it was going to have
Then, we called the output "x = " and we add the math function
Finally, we passed the values to solv_eq >> solv_eq("x + 8 = 5")'''





