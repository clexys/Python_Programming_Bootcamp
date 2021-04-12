'''
PROBLEM

Create an array of customer dictionaries
Output sample :

Enter Customer (Yes/No) : y
Enter Customer Name : Mike Altamirano
Enter Customer (Yes/No) : y
Enter Customer Name : Vashtie Cash
Enter Customer (Yes/No) : n
Mike Altamirano
Vashtie Cash

'''
# SOLUTION

# Create array (list) outside of the loop to be able to use it.
customers = []

# While True is used to loop indefinitely
while True:

    # Request user to make a choice
    create_entry = input("Enter Customer (Yes/No) : ")

    # create_entry[0] > This cuts the first char of whatever the user enter
    # The .lower() method, makes it lower case despite of what was entered
    create_entry = create_entry[0].lower()

    # Start the conditional to stop the loop when no more data needs
    # to be entered
    # WILL ADD EXCEPTION HANDLING IF USER ENTER ANY DIFF THAN YES OR NO
    if create_entry == "n":

        # Leave the while loop when n is entered
        break
    else:
        # Get the customer name by splitting at the space
        f_name, l_name = input("Enter Customer Name : ").split()

        # Add the dictionary to the array
        customers.append({'f_name': f_name, 'l_name': l_name})

# Print out customer list
for cust in customers:
    print(cust['f_name'], cust['l_name'])