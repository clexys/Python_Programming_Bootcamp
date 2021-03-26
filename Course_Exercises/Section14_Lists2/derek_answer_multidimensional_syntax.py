# This code multi_d_list = [[0] * 5 for i in range(4)]
# generates 5 columns and 4 rows in a multidimensional list with all being zero.

# multi_d_list is the lists name. [[0] * 5 for i in range(4)] says we want to make 4 rows and each row will have 5 columns. 
# Insert 0 into every space we create.

# It may help to think of a list as just a bunch of boxes. 
# A multidimensional list in this situation is 4 boxes with 5 boxes inside of each of the 4.

# This code might make more sense since the number of rows and columns is different.

for i in range(4):
    for j in range(5):
        multi_d_list[i][j] = "{} : {}".format(i, j)
# We take the 1st row and then we insert values in each column for that row. Then we switch to the 2nd row and repeat.

# The other code just outputs the list in an organized way. It isn't needed aside from that.

for i in range(4):
    for j in range(5):
        print(multi_d_list[i][j], end=" || ")
    print()
