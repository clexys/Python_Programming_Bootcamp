# Often when I'm trying to understand code it helps to output what is going on. I changed is_prime here to do that.

def is_prime(num):
    # This for loop cycles through primes from 2 to
    # the value to check
    for i in range(2, num):
    # If any division has no remainder we know it
    # isn't a prime number
        print(f"{num} % {i} = {num % i}")
        if (num % i) == 0:
            return False
    return True
# As you can see from the output i starts at 2 and then increases up to the value we are checking.
# Here is sample output



OUTPUT

Prime : 2

3 % 2 = 1

Prime : 3

4 % 2 = 0

5 % 2 = 1

5 % 3 = 2

5 % 4 = 1

Prime : 5



# gen_primes() is a weird function in that we tell it to generate all primes up to 50 with this line of code prime = gen_primes(50). 
# Then because it contains yield, each time we call next using our prime generator it finds and returns the next prime result.

# A generator is like a machine that produces products. We tell it we will only ever need primes up to 50, 
# but when we ask for another prime we want the machine to create the next prime. 
# There is no need for else ifs, since a number is either a prime In that case we want it. If it isn't a prime just discard it. Does that make sense?
