rows = int(input("Enter the height of the tree in feet here: "))

increments = list(range(1,rows*2,2)) #How hashes in each row increments

#print(increments)

largest_value = max(increments) #Last row with number of hashes

#print(largest_value)

i = 1

while i <= rows*2:

    if (i%2 != 0):

        print(' ' * (int((largest_value-i)/2)),(i*'#'))

        i += 1

        continue

    i +=1

print(' ' * (int((largest_value-1)/2)),'#')
