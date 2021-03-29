# Bubble Sort with a random list

# The Bubble sort is a way to sort a list. In it's simplest form, it arranges the list if it's
# out of order
# It works this way :
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index + 1]>>>
# This means check if the first item on the list is greater than the next item
# 5. If that is the case, we swap the index values. That means change the item's order
# 6. Therefore, when the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1, bcs we already know the largest number is at the end.

# Create the value that will decrement for the outer loop
# Its value is the last index in the list
# The below says, i equals the size of the list -1

import random

num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))
i = len(num_list) - 1
print(num_list)
while i > 1:
    j = 0

    while j < i:
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(num_list[j], num_list[j+1]))
        print()

        # If the value on the left is bigger switch values
        if num_list[j] < num_list[j+1]:
            print("Switch")

            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        # Track changes to the list
        for k in num_list:
            print(k, end=", ")
        print()
    print("END OF ROUND")

    i -= 1

for k in num_list:
    print(k, end=", ")
print()
