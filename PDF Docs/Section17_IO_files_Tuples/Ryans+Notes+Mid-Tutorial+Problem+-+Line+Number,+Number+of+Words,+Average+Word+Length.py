'''
For this problem I want you to cycle through each line of text and output the number of words
and the average word length. Here is sample output.
Line 1
Number of Words : 3
Avg Word Length : 4.7
Line 2
Number of Words : 3
Avg Word Length : 4.7
'''
# need the os module to deal with file i/o
import os
# create the mydata.txt with the words in it
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")
# open the file to read data
with open("mydata.txt", encoding="utf-8") as my_file:
    # need something to track line number, starting at 1
    # notice this is a global variable that will be
    # incremented in the while loop
    line_num = 1
    # loop to go line by line using readline()
    while True:
        # setting line to be the next line of the file
        line = my_file.readline()
        # if no more newlines, breaks the while loop
        if not line:
            break
        # prints the line number that we are tracking
        print("Line", line_num)
        # turn the line of words into a list of
        # words separated by spaces [.split()]
        list_words = line.split()
        # count the number of words and print it
        num_words = len(list_words)
        print("Number of Words :", num_words)
        # start a character count in the loops
        # you do not need this to be a global variable
        # since it is reset to 0 every iteration
        num_chars = 0
        # loops through each word in the list of words
        for word in list_words:
            # loops through each character in the specific word
            # being looked at in the list
            for char in word:
                # adds a character for each one
                num_chars += 1
        # takes the total number of characters and divides
        # by the total number of words to get the average
        # number of characters per word on the line and
        # prints that number to 1 decimal point
        avg_chars = float(num_chars/num_words)
        print("Avg Word Length : {:.1f}".format(avg_chars))
        # increments the line number for the next iteration
        line_num += 1