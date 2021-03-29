# We use while True any time we want to create an infinite loop that will end when we want it to. With this code :

while True:
    # We want a number and if we get one we hit break and the loop ends
    try:
        number = int(input("Please enter a number : "))
        break
 
    # If we don't get a number we execute this code and the loop continues
    except ValueError:
        print("You didn't enter a number")
 
    # This executes if some other error occurred
    except:
        print("An unknown error occurred")
