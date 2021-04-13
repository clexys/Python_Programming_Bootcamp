''' Basically, a recursive function is that calls itself.
It MUST contain to important parts > A recurrence relation and a termination condition
This last one, IS IMPERATIVE. Without a termination condition, we will have an infinite loop
(remember the while True?, well. IT'S THE SAME)

Also, Recursive Functions help us solve multiple problems with simple calculations repetitively, 
instead of writing a big block of code. '''

# We will calculate the factorial of 4 and see the code behind that operation
# function 4! = 3 * 2 * 1

# We create our factorial function
def factorial(num):

    # Defined the termination condition.
    if num <= 1:
        return 1
    # Executing the operation with the recursive function
    else:
        result = num * factorial(num - 1)
        return result
print(factorial(4))

# Here is how it works

# 1st : result = 4 * factorial(3) = 4 * 6 = 24
# 2nd : result = 3 * factorial(2) = 3 * 2 = 6
# 3rd : result = 2 * factorial(1) = 2 * 1 = 2