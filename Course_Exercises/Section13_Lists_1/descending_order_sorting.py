# PROBLEM

# SORT THE FOLLOWING LIST IN DESCENDING ORDER

# This is a given list
values = [20, 90, 30, 10, 300]

# We use the for loop to compare the values within the list and
# repeating loop for the range (number of times to repeat) given amount of values within the list
for comparing in range(len(values)):

    swapped = False
    comparing2 = 0
    # Comparing2, defines that index starting position for the while

    while comparing2 < len(values)-1:
        if values[comparing2] < values[comparing2+1]:

            values[comparing2], values[comparing2+1] = values[comparing2+1], values[comparing2]
            swapped = True

        comparing2 = comparing2+1

    if swapped == False:
        break
    print(values)