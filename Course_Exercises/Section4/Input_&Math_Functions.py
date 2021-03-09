import math
# ALWAYS REMEMBER when you use import you MUST reference the module to access methods

name = input('What is your name : ')
print('Hello', name)

# Here we say that num_1 and num_2 are equal to the numbers that will be entered.
# Split says that whatever is before the whitespace will be stored in num_1 and after the whitespace in num_2
num_1, num_2 = input('Enter 2 Numbers : ').split()
# Convert strings into (integers)
num_1 = int(num_1)
num_2 = int(num_2)
# Add the values entered and store in sum
sum_1 = num_1 + num_2

# Subtract the values and store in difference
difference = num_1 - num_2

# Multiply the values and store in product
product = num_1 * num_2

# Divide the values and store in quotient
quotient = num_1 / num_2

# Use modulus on the values to find the remainder
remainder = num_1 % num_2

# format() loads the variable values in order inside the brackets
'''I can change the order in which the numbers print. However, they will always follow 
the original operation order
'''

print("{} - {} = {}".format(num_2, num_1, difference))
print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} % {} = {}".format(num_1, num_2, remainder))

# Problem to solve
'''
I want you to write a program that:

Asks the user to input the number of miles
You’ll convert miles to kilometers (kilometers = miles * 1.60934)
Then print this for example 5 miles equals 8.0467 kilometers
'''

#MyGuess

# miles = input("Enter the number of miles : ")
# miles = int(miles)
# kilometers = miles * (1.691)

# print("miles equals kilometers, (miles, kilometers)
      

#TODO : Find exercies to solve another time. Need more practic!!!


#The actual solution .... I was kinda close, but far ajajajja
miles = input('Enter Miles ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 times miles
kilometers = miles * 1.60934

# Print results using format()
print("{} miles equals {} kilometers".format(miles, kilometers))   
      
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
      
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = Multiply number in sequence e.g 1*2*3*4 etc
print("factorial(6) = ", math.factorial(6))

# Returns remainder of division
print("fmod(5,4) = ", math.fmod(5,4))

# Receives a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,5) = ", math.pow(2,5))

# Return the square root
print("sqrt(8) = ", math.sqrt(8))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# Defining base 10 and powering it e.g 10^3 = 1000
print("log(1000,10) = ", math.log(1000,10))


# Using base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# DONT FORGET TO CALL MATH BEFORE THE FUNCTIONS E.G math.cosh
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh
# They follow this format
print("sin(0) ", math.sin(0))

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))
      
