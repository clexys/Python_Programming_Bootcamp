import random

# While loops are used when you don't know how many times you will have to loop

#rand_num = random.randrange(1, 51)
#i = 1
#while i != rand_num:
    #i += 1
#print("The random value is : ", rand_num)


# Another way of doing it
# import random
# rand_num = random.randrange(1, 51)
# i = 1
# while i != rand_num:
 #   i += 1
# print("The random value is : ", i)

# Break & Continue

# Continue stops executing the code that remains in the loop and jumps back to the top and starts all over again
# Break ends execution and jumps directly to the code that lies immediately outside of the loop

# Here we’ll cycle from 0 to 20 with a while loop
# If a number is even will use continue to skip printing it
# If it is odd we’ll print it
# We’ll then end execution with break if the value ever reaches 15

# i is set as the starting value!!! MUST be define outside of the loop and it imperative we do it,
# Otherwise, it will fail
#i = 1
#while i <= 20:
    # If a number is even don't print it
    # if (i % 2) == 0:
      #  i += 1
       # continue

    # If i equals 15 stop looping
    # if i == 15:
      #  break

    # print("Odd : ", i)
    # Increment i
    # i += 1

    # Print the odds
    # It actually prints bcs you're telling the system to print while it's inside of
    # the loop. So the process is,
    # Loops to find odds, break if it find a 15, and prints the results of the loop.
    # That's why elif is not needed here

# PROBLEM
# He wants us to draw a pine tree after asking the user for the number of rows
# Basically, asking how tall is the tree.

# TIP 1

# Im going to need a while and 3 for loops

'''Tip 2
I know that this is the number of spaces and hashes for the tree
4 - 1
3 - 3
2 - 5
1 - 7
0 - 9
Spaces before stump = Spaces before top
'''

'''
TIP 3

You will need to do the following in your program : 

1. Decrement spaces by one each time through the loop
2. Increment the hashes by 2 each time through the loop
3. Save spaces to the stump by calculating tree height - 1
4. Decrement from tree height until it equals 0
5. Print spaces and then hashes for each row
6. Print stump spaces and then 1 hash
'''

tree_height = input("How Tall Is Your Tree : ")
tree_height = int(tree_height)
spaces = tree_height-1
hashes = 1
stump_spaces = tree_height-1
while tree_height != 0:
    for r in range(spaces):
        print(' ', end="")

    for r in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for r in range(stump_spaces):
    print(" ", end="")
print("#")
