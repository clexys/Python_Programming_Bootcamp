# Conditional Operators
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

''' ALWAYS the conditional needs to be followed by a colon ":" that 
goes after the option provided'''

#drink = input("Pick One (Coke, or Pepsi) : ")
#if drink == "Coke":
   # print("Here is your Coke")
#elif drink == "Pepsi":
    #print("Here is your Pepsi")
#else:
    #print("Here is your water")
    

# Python Problem

# Accept 2 numbers separated by an operator 
# Then, use conditionals to determine what calculation to make
# SAMPLE OUTPUT: 
# Enter Calculation : 5 * 6
# 5 * 6 = 30
# Got completely lost on this one. Needed to follow the video to do it. 

# Store the user input of 2 numbers and the operator
# REMEMBER TO USE SPLIT with the delimiter of the space, otherwise, will fail
#num1, operator, num2 = input('Enter Calculation: ').split()

# ALWAYS Convert the string (input is always considered a string) into integers
#num1 = int(num1)
#num2 = int(num2)

# If, else if (elif) and else execute different code depending on a condition
#if operator == "+":
    #print("{} + {} = {}".format(num1, num2, num1+num2))

# If the 1st condition wasn't true check if this one is 
# (That is exactly what elif does)
#elif operator == "-":
    #print("{} - {} = {}".format(num1, num2, num1 - num2))
#elif operator == "*":
    #print("{} * {} = {}".format(num1, num2, num1 * num2))
#elif operator == "/":
    #print("{} / {} = {}".format(num1, num2, num1 / num2))

# If none of the above conditions were true then do this by default
#else:
    #print("Use either + - * or / next time")

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
# Checks if the age is less than 65
# This is the same as if we put age > 65
elif not (age < 65):
    print("Important Birthday")
else:
    print("Sorry Not Important")

# Python problem 2
''''Determine what grade they should go
 depending on age'''

'''1. Age 5 go to Kinder
   2. Ages 6-17 go to grades 1 through 12
   3. Older than 17, "Go to college" '''

age = int(input("Enter your kid's age : "))

if age < 5:
    print("Still to young")
elif age == 5:
    print("Goes to Kinder")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to Grade {}".format(grade))
else:
    print("Go to college perro")

# Ternary Operator
# The ternary operator is used to assign one value or another based on a condition
# It follows this format condition_true if condition else condition_false

age = int(input("What is your age? "))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)






