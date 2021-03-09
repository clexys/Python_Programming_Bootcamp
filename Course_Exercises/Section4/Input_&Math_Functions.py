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

miles = input("Enter the number of miles : ")
miles = int(miles)
kilometers = miles * (1.691)

print("miles equals kilometers, (miles, kilometers)
      

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
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5,4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2,2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))


      
      
      
      
