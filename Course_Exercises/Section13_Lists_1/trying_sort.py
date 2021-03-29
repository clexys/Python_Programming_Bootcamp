values = [10, 20, 30, 90, 300]
for i in range(5):
    i = len(values) - 1
print(values)
while i > 1:
    j = 0

    while j < i:
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(values[j], values[j+1]))
        print()

        # If the value on the left is bigger switch values
        if values[j] < values[j+1]:
            print("Switch")

            temp = values[j]
            values[j] = values[j + 1]
            values[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        # Track changes to the list
        for k in values:
            print(k, end=", ")
        print()
    print("END OF ROUND")

    i -= 1

for k in values:
    print(k, end=", ")
print()