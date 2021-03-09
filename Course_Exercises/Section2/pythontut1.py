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

