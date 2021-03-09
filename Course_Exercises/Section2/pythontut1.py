# Variable naming rules
# Start with letter or underscore
# Good practice is using _ and not camelCase

# sys, is a module. A module provide pre-written code to save yourself some time
import sys

my_age = 30
my_name = "Mike"

print("Hello", my_name)

''' We created the name variable and called it 
after it printed "Hello" '''

# STRING VARIABLE

# The String variable must contain double quotes
# Below is an example on how to print quoted statements within your string
# It works bcs we use the "escape sequence" (See Regex) 

string_1 = "\"This is a quote\""
print(string_1)


'''
Newline : \n
Backslash : \\
Single quote : \'
Backspace : \b
Tab : \t
'''
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*



print(sys.maxsize)
print(sys.float_info.max)

# Float max is not accurate it will give an error after the #15 digit printed
# Example below 

f1 = 1.111111111111111
f2 = 1.111111111111111

f3 = f1 + f2
print(f3)

# CASTING = Basically changing the data type

print("Cast ", type(int(5.4)))  # to int
print("Cast 2 ", type(str(5.4)))  # to string
print("Cast 3 ", type(chr(97)))  # to string
print("Cast 4 ", type(ord('a')))  # to int

# Make sure i am casting to the correct data type when working with variables
# Make sure to surround calculations with parentheses when they produce a single value
num_1 = "1"
num_2 = "2"
print("1 + 2 =", (int(num_1) + int(num_2)))
