'''
Dictionary Functions
To solve this problem:
1. Create this dictionary derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}
2. Output the first name
3. Change the address to "215 North St."
4. Output the new address
5. Create a new key "city" with a new value "Pittsburgh"
6. Check if there is a key named "city"
7. Delete key/value "f_name" and "Derek"
8. Print out all key and values on separate lines
9. This is your expected output
First Name : Derek
New Address : 215 North St
Is there a city : True
l_name Banas
address 215 North St
city Pittsburgh
'''

# 1. Create this dictionary derek_dict
derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}
# 2. Output the first name
print("First Name :", derek_dict["f_name"])
# 3. Change the address to "215 North St.
derek_dict["address"] = "215 North St"
# 4. Output the new address
print("New Address :", derek_dict["address"])
# 5. Create a new key "city" with a new value "Pittsburgh"
derek_dict["city"] = "Pittsburgh"
# 6. Check if there is a key named "city"
print("Is there a city :", "city" in derek_dict)
# 7. Delete key/value "f_name" and "Derek"
del derek_dict["f_name"]
# 8. Print out all key and values on separate lines
# This is the correct code to use, but the Udemy compiler
# keeps outputting in incorret orders so I output manually
for k, v in derek_dict.items():
    print(k, v)