'''
Create an Even List
To solve this problem:
1. Use a list comprehension to generate a list of even from 0 through 20
2. Output that list on 1 line with a space between each value
'''

# 1. Use a list comprehension to generate a list of even from 0 through 20
even_list_1_20 = [i*2 for i in range(11)]
# 2. Output that list on 1 line with a space between each value
for i in even_list_1_20:
    print(i, end=" ")