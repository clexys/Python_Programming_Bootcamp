# Conditional Operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

''' ALWAYS the conditional needs to be followed by a colon ":" that 
goes after the option provided'''

drink = input("Pick One (Coke, or Pepsi) : ")
if drink == "Coke":
    print("Here is your Coke")
elif drink == "Pepsi":
    print("Here is your Pepsi")
else:
    print("Here is your water")
    

# Python Problem

# Accept 2 numbers separated by an operator 
# Then, use conditionals to determine what calculation to make
# SAMPLE OUTPUT: 
# Enter Calculation : 5 * 6
# 5 * 6 = 30
# Got completely lost on this one. Needed to follow the video to do it. 

# Store the user input of 2 numbers and the operator
# REMEMBER TO USE SPLIT with the delimiter of the space, otherwise, will fail
num1, operator, num2 = input('Enter Calculation: ').split()

# ALWAYS Convert the string (input is always considered a string) into integers
num1 = int(num1)
num2 = int(num2)

# If, else if (elif) and else execute different code depending on a condition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

# If the 1st condition wasn't true check if this one is 
# (That is exactly what elif does)
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))

# If none of the above conditions were true then do this by default
else:
    print("Use either + - * or / next time")

''' LOGICAL OPERATORS '''


# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

# SAMPLE: Writing a program that will determine whether a birthday is important or not


# Range 
# 1- 18 
# 21, 50, > 65 --> Important
# Other than that --> Not important

# Ask for the age AND cast to an integer
## This helps eliminate the need for the additional line. Try to do it on the other lines when trying on Pycharm
age = int(input("Enter Age : "))

if (age >= 1) and (age <= 18):
    print("Important Birthday")
# If age is either 21 or 50 then it is true
elif (age == 21) or (age == 50):
    print("Important Birthday")
# We check if age is less than 65 and then convert true to false or vice versa
# This is the same as if we put age > 65
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")








