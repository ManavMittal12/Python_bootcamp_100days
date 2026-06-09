# **kwargs : Many keyword arguments

# when we use **kwargs, the arguments turn into a dictionary
# this dictionary basically represents each of the keyword arguments
# and their values.
# e.g.
# {'add': 3, 'mul': 4}
'''
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

    # or
    print(kwargs["add"])

calculate(add=3, mul=4) # the arguments are turned into kwargs
'''


# it lets me look through all the inputs and find the required one and do something

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


# e.g
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]    # to fix the error
        # we can use the get method
        self.model = kw.get("model", "GTR") # the benefit of .get() is if
        # it doesn't find a key, it will return None or a default value we provide
        # but not give error


my_car = Car(make="Toyota", model="Camry")
print(my_car.make)


# what if we don't specify an argument out of them
my_bad_car = Car(make="Nissan")
print(my_bad_car.model)   # it gave an error message cause it couldn't get hold of a value from the dictionary,
# because we passed only one keyword argument
