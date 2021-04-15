'''
This is to test what happens if you don't assign all of the arguments
In this case I will not put weight and then call it with a @property
'''
class Dog:
    # weight is set to 0
    def __init__(self, name="", height=0, weight=0):

        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    # Create a new Dog object, without a weight defined
    spot = Dog("Spot", 66)
    # calling the weight attribute
    print("The dog's weight is:", spot.weight)
    # setting the public (no underscores in the class) attributes
    spot.weight = 26
    print("The dog's weight is:", spot.weight)

main()