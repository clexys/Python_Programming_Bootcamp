# Here is sample output you should aim for
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

num_fib_vals = int(input("How many Fibonacci values should be found : "))

i = 1

# While i is less then the number of values requested
# continue to find more
while i < num_fib_vals:
    # Call the fib()
    fib_val = fib(i)

    print(fib_val)
    i += 1

print("All Done")