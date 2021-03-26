# FOR AND RANGE
# Conditionally execute till not true

# Looping thru a list. The syntax is:
# for >> the function
# in >> defines where it will be looping
for i in [2,4,6,8,10]:
    print("i =", i)


# RANGE
'''It creates a list starting at 0 and going all the way up
   to the number we define but not including that number. 
    For example'''

for i in range(10):
    print("i =", i)

i = 6
(i % 2) == 0
print("Is 6 even? : ", ((i % 2) == 0))

# PROBLEM

# Print all the odd numbers from 1-20

# MY GUESS

#for i in range(1, 20):
 #   print("Odd numbers : ", (i % 2 != 0))
 # I MISSED THE CONDITIONAL

# ACTUAL SOLUTION
for i in range(1, 20):
    if (i % 2 != 0):
        print(" Odd numbers=", i)

# Addt'l info about Floats

# How to cast into a float
your_float = input("Enter a float : ")
your_float = float(your_float)

# Use format to define the number of decimals displayed
# For 2 decimals I need to use {:.2f}
# For more or less decimals just change the number
# NOTE> THe system will round the last digit depending on input
print("Rounded to 3 decimals : {:.3f}".format(your_float))

# PROBLEM 2

'''Calculate how much money a person will have after investing for 10 years
Compounding interest is the act of reinvesting each years interest 
payment and then receiving interest on the initial value as well as on interest payments'''

# EXPECTATIONS :
# 1. Have the user enter their investment amount and expected interest
# 2. Each year their investment will increase by their investment + their investment * the interest rate
# 3. Print out their earnings after a 10 year period

# HOW I THINK IT SHOULD BE
# FINAL OUTPUT IS EMPTY. =,(
# NOW I KNOW WHY... I WAS MISSING THE BRACKETS!!!! DUH!! I WAS USING FORMAT

money = input("Decide your investment amount : ")
int_rate = input("Your account's interest rate : ")

money = float(money)
int_rate = float(int_rate) * .01

for X in range(10):
    money = money + (money * int_rate)

print("Your total earning over these 10 years is : ${} ".format(money))

# ACTUAL SOLUTION

# Ask for money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")

# Convert value to a float
money = float(money)

# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01

# Cycle through 10 years using for and range from 0 to 9
for i in range(10):
    # Add the current money in the account + interest earned that year
    money = money + (money * interest_rate)

# Output the results
print("Investment after 10 years: {:.2f}".format(money))

# ORDER OF OPERATIONS!!! REALLY IMPORTANT

# Calculations will occur in this order :
# 1. exponentiation and root extraction
# 2. multiplication and division
# 3. addition and subtraction

# EXAMPLES
print("2 + (3 * 4) =", (2 + (3 * 4)))
print("(2 + 3) * 4 =", ((2 + 3) * 4))
print("2 + (3 * 4) =", 2 + 3 * 4)