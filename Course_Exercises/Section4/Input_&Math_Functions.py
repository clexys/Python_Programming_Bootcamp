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
      
