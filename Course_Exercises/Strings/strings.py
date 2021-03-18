# Strings

# Strings are a series of characters between quotes. You can use Single quotes, double quotes or triple quotes.
print(type("3"))
print(type('3'))
print(type('''3'''))

# I can see the data type for data using type
print(type(3))
print(type(3.14))

# Each character is stored in a series of boxes labeled with index numbers
# You can find out how many characters a string contains
# len(name_of_string_variable) >> it allows me to know the amount 
# of characters the string has

samp_string = "This is a very important string"
print("Length :", len(samp_string))

# I can get characters using index numbers starting at 0
# samp_string[0] >> gives me first character 

samp_string = "This is a very important string"
print(samp_string[0])

# Gives me the last character
print(samp_string[-1])

# You can get a block of characters using slice
# A slice is where you define what index values 
# you want between 2 brackets
samp_string = "This is a very important string"
# Get a slice by saying where to start and where to end
# The 7th index isn't returned
print(samp_string[0:7])

# Get everything starting at an index position
print(samp_string[8:])

# More ways to slice
# The ":" at the end means I want to bypass 2 char when printing and the first line
# tells me the start and the end
print("Every Other ", samp_string[0:-1:2])

# By using 2 ":" you're telling
print("Reverse ", samp_string[::10])

# Join or concatenate strings with +
print("Green " + "Eggs")

# Repeat strings with *
print("Hello " * 5)

# Convert an int into a string
num_string = str(4)

# You can cycle through each character with for
samp_string = "This is a very important string"
for char in samp_string:
    print(char)

# You can cycle through characters in pairs
# Subtract 1 from the length because length is 1 more then the highest index because strings are 0 indexed
# Then use range starting at index 0 through string length and increment by 2 each time through
samp_string = "This is a very important string"
for i in range(0, len(samp_string)-1, 2):
    print(samp_string[i] + samp_string[i+1])

# Computers assign characters with a number known as a Unicode A-Z have the numbers 65-90 and a-z 97-122
# 2 functions allow you to work with unicodes
# You can get the Unicode code with ord()
print("A =", ord("A"))
# You can convert the Unicode number to a letter with chr
print("65 =", chr(65))

# Let's say you want to add val plus 1. You could type out val = val + 1, but there is a shortcut way val_1 += 1
# This shortcut can be used for all math operations

# val_1 = val_1 + 1
# val_1 -= 5
# val_1 *= 3
# val_1 /= 2
# val_1 %= 6

# Likewise you can also add one string to another in the same way
# str_1 += str_2

# Python Problem

# As Derek says, it doesn't matter if I don't get it right,
# The only goal is to understand the solution.
# Your code should receive a uppercase string and then hide its meaning by turning it into a string of unicodes
# Then it should translate the unicodes back into the original message 

# First, request the string to work with
norm_string = input("Enter a string to hide in uppercase: ")
# Here I define secret_string as "" bcs if I had assigned a value, it wouldn't print what I wanted
# bcs on line 105 I'm saying that it will be equal to the char converted to unicode
secret_string = ""

# Cycle through each character in the string
for char in norm_string:
    # Store each character code in a new string
    # += is the same as secret_string = secret_string + whatever
    # Here str(ord(char)) means
    # str - Converts what's inside of the () into a string type
    # ord - Converts "char" to Unicode characters
    secret_string += str(ord(char))

print("Secret Message :", secret_string)

norm_string = ""

# Cycle through each character code 2 at a time by incrementing by
# 2 each time through since Unicodes go from 65 to 90
for i in range(0, len(secret_string)-1, 2):
    # Get the 1st and 2nd for the 2 digit number
    char_code = secret_string[i] + secret_string[i+1]

    # Convert the codes into characters and add them to the new string
    norm_string += chr(int(char_code))
print("Original Message :", norm_string)

# 2nd Python Problem

# Make the above take input with upper and lowercase letters by changing 2 lines of code

# Add these 2 changes

secret_string += str(ord(char) - 23)
norm_string += chr(int(char_code) + 23)

# Had to take the examples from the course

# Take in a word
UCString = str(input("Please enter a word: "))
# Set the Unicode string to nothing at first
UNIString = str("")
# Convert string to unicode
# We are going to subtract 23 from the unicode to handle the lowercase letters that
# turn the ord into a triple digit (i.e. a - z is 97 - 122, hence d-z is over 100)
for i in UCString:
	UNIString += str(ord(i) - 23)
# Print the Unicode String as unicode
print("Unicode String is:", UNIString)
print("Note: All double digit values are 23 less than the real unicode values")
# Sets the UPPEPRCASE word to nothing in order to reset it from the unicode
UCString = str("")
# Loops the Unicode back into the UPPERCASE word string 1 letter at a time
# Needs to pull in 2 at a time in order to get both digits of the unicode (65 - 90 for A - Z)
for i in range(0, len(UNIString) - 1, 2):
    # char will be 2 digits
    char_UNICODE = UNIString[i] + UNIString[i+1]
    # Adds each char individually based on the 2 digit unicode
    # We add the 23 back to the unicode value because we removed it earlier to
    # make the char_UNICODE only pull 2 digit values
    UCString += chr(int(char_UNICODE) + 23)
# prints the original UCString
print("The original word:", UCString)
