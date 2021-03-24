# Get the functions to do 2 things at a time>> Multiply and Divide in this case
# To do this, we use return and specify the operations and separate them with a comma

def mult_div(num_1, num_2):
    return (num_1 * num_2), (num_1 / num_2)
# THen we say that mult and div (the variables) are equal to our function. Still, it is
# IMPORTANT that we separate them with a comma


mult, divide = mult_div(5, 4)

# Finally, we print the results.
print("5 * 4 =", mult)
print("5 / 4 =", divide)


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True


def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes


max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)

# We can receive an unknown number of arguments using the splat (*) operator
# ALWAYS be careful not to use a conflicting name like "sum"
# bcs it will cause the program to break without apparent reason
# and the program will not show ANY type of error or warning
# ALSO, BE EXTREMELY CAREFUL WITH INDENTATION...
# return sum_mike was not working bcs it was inside the loop and it was
# supposed to be outside

def sum_todo(*pico):
    sum_mike = 0
    for i in pico:
        sum_mike += i
    return sum_mike

print("Sum :", sum_todo(1, 2, 3, 4))

def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1

print("Sum :", sum_all(1, 2, 3, 4))

# FUNCTIONS TO CALCULATE AREAS OF DIFFERENT TYPES OF SHAPES

# Here we will route to different functions depending on what type of shape we want to get the area for
# We will also use a main function for the first time
import math

# This routes to the correct area function
# The name of the value passed doesn't have to match
def get_area(shape):

    # Switch to lowercase for easy comparison
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

# Create function that calculates the rectangle area
def rectangle_area():
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))

    area = length * width

    print("The area of the rectangle is", area)


# Create function that calculates the circle area
def circle_area():
    radius = float(input("Enter the radius : "))

    area = math.pi * (math.pow(radius, 2))

    # Format the output to 2 decimal places
    print("The area of the circle is {:.2f}".format(area))

# We often place our main programming logic in a function called main
# We create it this way
def main():

    # Our program will calculate the area for rectangles or circles

    # Without functions we'd have to create a giant list of ifs, elifs

    # Ask the user what shape they have
    shape_type = input("Get area for what shape : ")

    # Call a function that will route to the correct function
    get_area(shape_type)

    # Because of functions it is very easy to see what is happening
    # For more detail just refer to the very short specific functions

# All of the function definitions are ignored and this calls for main()
# to execute when the program starts

# I THINK THAT DEREK'S INTENTION WAS TO DEMONSTRATE THAT WE CAN MAKE A BLOCK OF CODE
# AT ANY POINT AND EXECUTE BEFORE ANYTHING ELSE.

main()