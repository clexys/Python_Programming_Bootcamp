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

