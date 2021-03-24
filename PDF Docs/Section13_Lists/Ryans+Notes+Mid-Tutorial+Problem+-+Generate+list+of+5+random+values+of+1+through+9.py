'''
Generate a list with 5 values from 1-9
'''
# Must have the random module to do random value generation
import random
# need a list that can be appended with new values
list_of_rand_values = []
# create a for loop with 5 values
for i in range(5):
    # create a random number 1-9
    rand_value_1to9 = random.randrange(1, 10)
    # append the list values using the random range generation
    list_of_rand_values.append(rand_value_1to9)
# Need a for loop to cycle through the indexes and print them
for i in list_of_rand_values:
    # prints each index on each loop iteration, separated by spaces
    print(i, end=" ")