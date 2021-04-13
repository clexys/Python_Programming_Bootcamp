# To test what you have learned I now want you to calculate Fibonacci numbers.

# To calculate Fibonacci numbers we sum the 2 previous values to calculate the next item in the list like this 1, 1, 2, 3, 5, 8 ...

# The Fibonacci sequence is defined by:
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result
# Note:
# Here the digit inside of fib(), defines the
# position on the Fibonacci sequence, NOT the index position.
print(fib(6))

print(fib(4))
