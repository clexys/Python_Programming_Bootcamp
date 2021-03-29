'''
With 2 for loops fill the cells in a multidimensional list with a
multiplication table using values 1 - 9. This is your goal.
'''
# Creates a blank 10 x 10 2-dimension list
mult_table = [[0] * 10 for i in range(10)]
# print(mult_table)
# Outer loop (columns) for 1-9, must be rage(1, 10) or will have zeros
for i in range(1, 10):
    # Inner loop (rows) for 1-9, must be rage(1, 10) or will have zeros
    for j in range(1, 10):
        # Multiplies i by j, starting with 1 * 1 and ending with 9 * 9
        mult_table[i][j] = i * j
        # Prints i * j with a comma at the end (not new line)
        print(mult_table[i][j], end=", ")
    # Prints a new line between loop between row iterations
    # so the new column will have a new line, otherwise it
    # will just run the whole table together in one row
    print()