# It doesn't matter where the main function is in your file. Unlike other languages main isn't called automatically with Python.

# When a Python file is executed it looks for code to execute. It ignores all the code found in functions however.

# So if my code was just this nothing would happen.

def main():
    shape_type = input("Get area for what shape : ")
    get_area(shape_type)
# However this line of code calls for the main function to execute. It is actually the only code outside of a function.

main()

# I'll just abbreviate the functions in the examples. If pass is used in a function, when the function is called nothing happens. 
# It is used to think out what your functions names and parameters will be and then you go back and fill in the code later. If I have

# 5. This function calls the correct area function
def get_area(shape):
    pass
# 6a. If the string was "rectangle" execute this function
def rectangle_area():
    pass
# 6b. If the string was "circle" execute this function
def circle_area():
    pass
# 2. main executes
def main():
    # 3. Get a string representing what area to calculate
    shape_type = input("Get area for what shape : ")
    # 4. Call the proper area function based on the string
    get_area(shape_type)
 
# 1. Calls for the main function to execute
main()
 
# 7. There is no more code so end the programs execution
I hope that helps

Derek
