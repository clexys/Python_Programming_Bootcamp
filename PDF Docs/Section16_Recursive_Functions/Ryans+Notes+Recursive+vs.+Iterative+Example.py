'''
Recursive version of the Factorial program that shows how it works in each iteration
'''
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        print("Hit exit condition n = 1, returns 1")
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial( n-1 = ", n-1, "): ",res)
        return res

print("Recursive Factorial of 5 :".upper())
print()
print(factorial(5))
print("\n\n\n")

'''
Iterative version of the Factorial program that shows how it works in each iteration
'''
def iterative_factorial(n):
    res = 1
    for i in range(2,n+1):
        print("factorial has been called with n = " + str(i))
        res *= i
        print("intermediate result for res *= i : ", res)
    return res

print("Iterative Factorial of 5 :".upper())
print()
print(iterative_factorial(5))