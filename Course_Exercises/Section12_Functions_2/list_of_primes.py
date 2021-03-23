# First, we create our function and pass it to the value of num
# The for loop cycles from 2 to the value to check\
# NOTE> The first part is really important bcs without it the res
# of the code breaks

def is_prime(num):
    for i in range(2, num):
        # Below, if the division has no remainder, then it
        # isn't a prime
        # Waiting on Derek's response to comment this part
        if (num % i) == 0:
            return False
        return True

# Here define another function to get the prime numbers
def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes

max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)
