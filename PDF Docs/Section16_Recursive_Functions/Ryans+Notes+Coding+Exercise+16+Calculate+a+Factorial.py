'''
Create a Factorial
To solve this problem:
1. Create a function that will find the factorial for a value using a recursive function.
Factorials are calculated as such 3! = 3 * 2 * 1
2. Expected Output
Factorial of 4 = 24

Factorial at its recursive form is: X! = X * (X-1)!
'''
# define the factorial function
def factorial(n):
    # Sets to 1 if asked for 1
    # This is the exit condition
    if n==1:
        return 1
    else:
        # factorial in recursive form for >= 2
        result = n * factorial(n-1)
        return result
# prints factorial of 4
print ("Factorial of 4 =", factorial(4))