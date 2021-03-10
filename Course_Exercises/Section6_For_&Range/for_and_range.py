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

for i in range(6):
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
