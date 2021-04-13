import os
with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")
    myFile.write("\n\n\n\n")
    myFile.write("HIIIIIIII\n\n\n\n")

with open("mydata.txt", encoding="utf-8") as my_file:
    # continues loops until a line reads back as False (no more newlines)
    while True:
        # sets line to the next line of text
        # readline() works one line at a time when called
        line = my_file.readline()
        # When line returns False (or empty) it stops the loop
        if not line:
            break
        print(line, end="")