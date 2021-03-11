# Here I will learn what to do in cases like https://github.com/Ilikef150s2/Python_Programming_Bootcamp/blob/8aaebe667408c4a4ab02f6d5ab84e1da6e212d14/Course_Exercises/Section5_Conditionals/Conditionals.py#L23
# where the input is completely unexpected

while True:
    # If we expect an error can occur surround potential error with try
    try:
        number = int(input("Please enter a number : "))
        break
        #The code here will break bcs we can't cast "dog" into an int

    # The code in the except block provides an error message to set things right
    # We can either target a specific error like ValueError
    except ValueError:
        print("You didn't enter a number")

    # We can target all other errors with a default
    except:
        print("An unknown error occurred")
print("Thank you for entering a number")

