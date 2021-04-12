# Dictionaries

#Unlike lists, they use pair of key - values. Structure is 
# fName : "Mike" >> fName is the key; "Mike" is the value

mike_dict = {'first_name': 'Mike', "last_name": "Altamirano",
            "phone":"58496194"}
# first we define the name mike_dict =
# Then, we put everything insie {} and use either single or double quotations ('' OR "" MAKE NO DIFFERENCE)
# for the key and the value
# key and value MUST be separated by a " : "
# To get the info on screen, we use print. We put the string text we want to show
# Then, we call our dict and within " [] " we call the key we want to use
print("My Name :", mike_dict["first_name"])

# Change Dictionary values
# We call the dict and the key. Then, we use " = " and put the new value
# Within "" without the []

mike_dict["phone"] = "57165948"

# Add Dictionary Keys and Values
# We call the dictionary and put the key inside [] and we put the new value# within "" without the []

mike_dict["city"] = "Managua"

# To check if the key was added, we use print and call the it by
# entering the key name, the word "in" and the dict name
# Doing that, will return either True or False
# Optionally, you can print add a question prior to the value (for visualization)
# but it is not mandatory nor necessary
print("Is there a city? : ", "city" in mike_dict)

# Print a list of my dict values

print(mike_dict.values())

# Print a list of my dict keys
print(mike_dict.keys())

# Print both of them together
# .items() method will allow us get all the items within our dic for the loop

for keys, values in mike_dict.items():
    print(keys, values)

# Get a value from a key

print(mike_dict.get("second_name", "Not Found"))

print(mike_dict.get("city", "Not Found"))

# Delete a key value

del mike_dict["first_name"]

# Loop thu the dictionary
for i in mike_dict:
    print(i)

# Delete the WHOLE dictionary
mike_dict.clear()
print(mike_dict.get("city", "Not Found"))

# CREATE A LIST TO HOLD A DICTIONARY

# We create the empty list first,
employees = []

# Then, we create our variables and use input to get request data from the user
first_name, last_name = input("Enter Employees Name: ").split()

# Here we use the append method to add the values we stored (in
# first_name and last_name) and pass them on to our keys we will create
employees.append({"first_name": first_name, "last_name": last_name})
print(employees)

'''
PROBLEM

Create an array of customer dictionaries
Output sample : 

Enter Customer (Yes/No) : y
Enter Customer Name : Mike Altamirano
Enter Customer (Yes/No) : y
Enter Customer Name : Vashtie Cash
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''
# SOLUTION
# Create customer array outside the for so it isn't local
# to the while loop
customers = []

while True:
    # Cut off the 1st letter to cover if the user
    # types a n or y
    create_entry = input("Enter Customer (Yes/No) : ")
    create_entry = create_entry[0].lower()

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