'''
Solving Equations with a Function
How to solve this problem:
Don't use the input function in this solution
1. Create a function named solve_eq that receives equations like this "x + 4 = 9"
2. solve_eq will solve for x and turn output such as "x = 5"
'''

# define the function named solve_eq that takes in the string
def solve_eq(equation):
    # Turn the string into the numbers that are being subtracted
    # to solve for x using the indexes of the input numbers.
    # num_1 is the 4, num_2 is the 9
    num_1 = int(equation[4])
    num_2 = int(equation[8])
    # return x = num_2 - num_1
    return "x = " + str(num_2 - num_1)
# Have to print the function that was run, if you just
# run the function it doesn't print x = 5
print(solve_eq("x + 4 = 9"))

# There is a major weakness in my program when I did it vs. Derek's.
# This one would only be able to handle single digit solving of x.