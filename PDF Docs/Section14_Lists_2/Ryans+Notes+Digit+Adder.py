'''
A function that does:
Gets a user input which is a string.
The string contains both numbers and letters.
e.g  string = 'ytyudk5u9hfbd45'
How does one take the numbers out of the string, and add them together? In this case: ytyudk5u9hfbd45
Take numbers out of the string and 5+9+4+5 and return the answer?
'''

# Derek's Answer:
# Get string that contains numbers
str_1 = input("Enter a String : ")
sum_1 = 0
i = 0
# Cycle through string till the end
while i < len(str_1):
    # Check if string is a number
    if str_1[i].isdigit():
        # If it is add to sum
        sum_1 += int(str_1[i])
    i += 1

print(f"Sum : {sum_1}")

# Peter's first answer
string = 'ytyudk5u9hfbd45'
sum1 = 0
for i in string:
    if i.isdigit():
        sum1 += int(i)
print(sum1)

# Peter's List Comprehension version:
#This creates a list of digits as ingetegers
sum1 = [int(i) for i in string if i.isdigit()]
sum2 = 0
# adds up the integers
for i in sum1:
    sum2 += i
print(sum2)

# Peter's even shorter answer
string = 'ytyudk5u9hfbd45'
sum1 = [int(i) for i in string if i.isdigit()]
print(sum(sum1))

# My EVEN SHORTER (1 line special edition) version lol
print(sum([int(i) for i in 'ytyudk5u9hfbd45' if i.isdigit()]))

# My EVEN SHORTER version with input
print("Sum:", sum([int(i) for i in input("Enter random letters and numbers: ") if i.isdigit()]))