'''
To test what you have learned I now want you to calculate Fibonacci numbers.
To calculate Fibonacci numbers we sum the 2 previous values to calculate the next item in the
list like this 1, 1, 2, 3, 5, 8 ...
The Fibonacci sequence is defined by:
Fn = Fn-1 + Fn-2
Where F0 = 0 and F1 = 1
Here is a sample run through to help
print(fib(3))
1st : result = fib(2) + fib(1) : 2 + 1
2nd : result = (fib(1) + fib(0)) + (fib(0)) : 1 + 0
3rd : result = fib(2) + fib(1)
print(fib(4))
1st : result = fib(3) + fib(2) : 3 + 2
2nd : result = (fib(2) + fib(1)) + (fib(1) + fib(0)) : 2 + 1
3rd : result = (fib(1) + fib(0)) + fib(0) : 1 + 0
Give it a try. The goal is to get you to think in new ways and to understand the final result.

Second part is to create an input to ask for how many values you want and print them.
'''
# It will go through and do fib(num) = fib(num-1) + fib(num-2)
# As it iterates (recursively) it will will break down each successive
# fib sequence until it hits 0
# define the function
def fib(num):
    # sets to return 0 to the function when num = 0
    # This is what allows the recursion to do the fib(num - 2)
    # otherwise it wouldn't be able to do the recursion for num <= 2
    if num == 0:
        return 0
    # sets to return 1 to the function when num = 1
    # This is what allows the recursion to do the fib(num - 1)
    # otherwise it wouldn't be able to do the recursion for num <= 2
    if num == 1:
        return 1
    # sets to return the result to the function when num >= 2
    # the result will be fib of (num-1) + (num-2)
    else:
        result = fib(num - 1) + fib(num - 2)
        return result
'''
# prints the 1st 10 fib values
for i in range(10):
    print(fib(i),end=" ")
'''
fib_values = input("How many values of the Fibonacci values do you want : ")
for i in range(int(fib_values)):
    print(fib(i),end=" ")