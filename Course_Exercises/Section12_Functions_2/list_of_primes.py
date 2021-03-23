# First, we create our function and pass it to the value of num
# The for loop cycles from 2 to the value to check\
# NOTE> The first part is really important bcs without it the res
# of the code breaks

def is_prime(num):
    for i in range(2, num):
        # i toma el valor de 2, xq es el primer number por el q empieza el ciclo
        # Luego, num se divide entre el primer valor de i (osea 2)
        if (num % i) == 0:
            return False
        return True
    # In the above example, (num % i) == 0 is the test expression.
    # The body of "if" is executed only if this evaluates to True.
    # When the result of variable (num % i) is equal to 0, test expression is
    # False and statements inside the body of if are executed.
    # If the result is != 0, test expression is false and statements inside the body of if are skipped.


# Here define another function to get the prime numbers
def get_primes(max_number_req):
    # Below we create an empty list to hold our primes
    list_of_primes = []
    # This loop is gon' to cycle from 2 to the max num that is req
    for num_1 in range(2, max_number_req):
        # We call our is_prime function
        # Then we pass that onto our num_1
        if is_prime(num_1):
            list_of_primes.append(num_1)
            # If the result of is_prime is true, then we add it to the empty list we did before by
            # calling it and using the append
    return list_of_primes


# Lastly, we created a variable called max_num_to_check that will take the input.
max_number_req = int(input("Search for Primes up to : "))

# Then, we define that our empty list_of_primes will contain what we get from max_num_to_check
list_of_primes = get_primes(max_number_req)

# Finally, we cycle thru our list and store the info into prime and we print it
for prime in list_of_primes:
    print(prime)
