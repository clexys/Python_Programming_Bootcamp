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

# Now, let's try to use the same function by asking the input from the user

def mult_div(num_1, num_2):
    input("Enter the 2 number you want to mult and div: ", num_1, num_2)

    # Testing git
Trying again.....
AND TRYING AGAIN..... 
