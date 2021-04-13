# SAMPLE OUTPUT
# How many Fibonacci values should be found : 30
# 1
# 1
# 2
# 3
# 5
# All Done

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

amount_fib_values = int(input("How many Fibonacci values should be found : "))

# Here we define the number the list should start off.
i = 0

# While i is less then the number of values requested
# continue to find more
while i < amount_fib_values:
    # Call the fib() we defined above
    fib_val = fib(i)

    print(fib_val)
    # Remember, we should always do i +=1 to move or increase one
    # position after every loop, otherwise, we'd had an infinite loop.
    i += 1

print("All Done")