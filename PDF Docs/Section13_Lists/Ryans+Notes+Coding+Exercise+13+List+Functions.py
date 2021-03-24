'''
List Functions
To solve this problem:
1. Make a list that contains the values 5, 2, 9, 1 named my_list
2. Make a list using range with values 0, 1, 2, 3, 4
3. Output the following using the list functions
Length : 4
1st Index : 5
1st 3 Values : [5, 2, 9]
9 in List : True
Index for 2 : 1
How Many 2s : 1
4. Remove the 1 value from my_list
5. Remove the first index in my_list
6. Insert 10 in the first index
7. Print the sorted list and the reverse list like this
Sorted : [2, 9, 10]
Sorted : [10, 9, 2]
'''
# 1. Make a list that contains the values 5, 2, 9, 1 named my_list
my_list = [5, 2, 9, 1]

# 2. Make a list using range with values 0, 1, 2, 3, 4
range_list = list(range(5))
#print(range_list)

# 3. Output the following using the list functions
# Length : 4
print("Length :", len(my_list))
# 1st Index : 5
print("1st Index :", my_list[0])
# 1st 3 Values : [5, 2, 9]
print("1st 3 Values :", my_list[0:3])
# 9 in List : True
print("9 in List :", 9 in my_list)
# Index for 2 : 1
print("Index for 2 :", my_list.index(2))
# How Many 2s : 1
print("How Many 2s :", my_list.count(2))

# 4. Remove the 1 value from my_list
my_list.remove(1)

# 5. Remove the first index in my_list
my_list.pop(0)

# 6. Insert 10 in the first index
my_list.insert(0, 10)

# 7. Print the sorted list and the reverse list like this
# Sorted : [2, 9, 10]
my_list.sort()
print("Sorted :", my_list)
# Sorted : [10, 9, 2]
my_list.reverse()
print("Sorted :", my_list)