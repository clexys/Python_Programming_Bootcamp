''' Python is an OOP Language (Object Oriented Programming)
OOP is the act of modeling a real world object with code.  
Now, real world objects have attributes and capabilities.
'''

# ATTRIBUTES            Capabilities
# Height,               1. Talk
# Weight,               2. Walk
# Name, etc             3. Eat

# Attributes are stored in variables called Fields
# We model capabilities using functions which are called methods.

# A class is a blueprint we use to define an
# objects attributes (fields) and capabilities (methods).

# Here we will model a Dog object.

# Start by defining the objects name with
class Dog:
    # The init method is called to create an object
    # With it, we set all values required when a new object is created
    # We give default values for the fields if none
    # are provided
    def __init__(self, name="", height=0, weight=0):
        # self allows an object to refer to itself bcs we don't know
        # what the user will call his "Dog" later
        # It is like how you refer to yourself with my

        # We will take the values passed in and assign
        # them to the new Dog objects fields (attributes)
        self.name = name
        self.height = height
        self.weight = weight

    # Define what happens when the Dog is asked to
    # demonstrate its capabilities

    # The function is defined
    def run(self):
        # We use format to pass the value of the fields
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    # Create a new Dog object

    # The values inside "Dog" are the attributes we defined above
    # Spot = Name, 66 = Height, 26 = Weight
    # If you want to change the dog's name, just do it inside the string
    spot = Dog("Chris", 66, 26)
    # We call the bark function with out new Dog name
    spot.bark()

main()
