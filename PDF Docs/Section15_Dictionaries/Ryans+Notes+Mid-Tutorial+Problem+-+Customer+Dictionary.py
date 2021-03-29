'''
Create an array of customer dictionaries and the output should look like this :
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith

It will keep asking for more until n is entered
'''

'''
# original attempt before realizing I created a LIST OF DICTIONARIES
# NOT a dictionary that I wanted to add more to
# defaults as y so that the loop starts
more_customers = "y"
# customer counter for the key value, starts at 1
customer_count = 1
# create the empty list for the dictionaries
# This is NOT a dictionary, but instead a list of dictionaries
customers = []
# create a while loop for when more_customers isn't n:
while more_customers != "n":
    # Asks if they want to add a customer each loop iteration
    # including the original run of it
    more_customers = input("Enter Customer (Yes/No) : ")
    more_customers = more_customers[0].upper()
    # Checks for a y or n and prompts again if not
    while more_customers != "Y" and more_customers != "N":
        more_customers = input("Enter Customer (Yes/No) : ")
    if more_customers == "N":
        break
    # have them enter the name
    customer = input("Enter Customer Name : ")
    # add the customer to the dictionary
    customers.append({customer_count : customer})
    # adds 1 to the customer count, sort of like an index
    customer_count += 1
# resets customer_count to 1 for the loop
customer_count = 1
# prints the list of customers on separate lines
for i in customers:
    print(i[customer_count])
    customer_count += 1
'''
'''
# Improved way of the above program
# The customer_count isn't necessary
# defaults as y so that the loop starts
more_customers = "y"
# create the empty list for the dictionaries
# This is NOT a dictionary, but instead a list of dictionaries
customers = []
# create a while loop for when more_customers isn't n:
while more_customers != "n":
    # Asks if they want to add a customer each loop iteration
    # including the original run of it
    more_customers = input("Enter Customer (Yes/No) : ")
    more_customers = more_customers[0].upper()
    # Checks for a y or n and prompts again if not
    while more_customers != "Y" and more_customers != "N":
        more_customers = input("Enter Customer (Yes/No) : ")
    if more_customers == "N":
        break
    # have them enter the name
    customer = input("Enter Customer Name : ")
    # add the customer to the dictionary
    customers.append({"name" : customer})
# prints the list of customers on separate lines
for i in customers:
    print(i)            # This returns the dictionary { key : value }
    print(i["name"])    # This returns the value
    for k in i:
        print(k)        # This returns the key
        print(i[k])     # This also returns the value
'''

# defaults as y so that the loop starts
more_customers = "y"
# create the empty dictionary
# This is NOT a list of dictionarys, but instead a single dictionary
customers = {}
# customer counter for the key value
customer_count = 0
# create a while loop for when more_customers isn't n:
while more_customers != "n":
    # Asks if they want to add a customer each loop iteration
    # including the original run of it
    more_customers = input("Enter Customer (Yes/No) : ")
    # Checks for a y or n and prompts again if not
    while more_customers != "y" and more_customers != "n":
        more_customers = input("Enter Customer (Yes/No) : ")
    if more_customers == "n":
        break
    # adds 1 to the customer count, sort of like an index
    customer_count += 1
    # have them enter the name
    customer = input("Enter Customer Name : ")
    # add the customer to the dictionary
    customers[customer_count] = customer
# prints the list of customers on separate lines
for k, v in customers.items():
    print(v)