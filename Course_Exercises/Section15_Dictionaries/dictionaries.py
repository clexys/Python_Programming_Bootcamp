# Dictionaries

#Unlike lists, they use pair of key - values. Structure is 
# fName : "Mike" >> fName is the key; "Mike" is the value

mike_dict = {"first_name": "Mike", "last_name": "Altamirano",
            "phone":"58496194"}
# first we define the name mike_dict =
# Then, we put everything insie {} and use double quotations for the key and the value
# key and value MUST be separated by a " : "
# To get the info on screen, we use print. We put the string text we want to show
# Then, we call our dict and within " [] " we call the key we want to use
print("My Name :", mike_dict["first_name"])