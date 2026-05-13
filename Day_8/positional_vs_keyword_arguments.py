# Positional vs Keyword Arguments
# We created a function that allows for an input
# Here, we'll create a function that takes multiple inputs

# Functions with more than 1 input
# this will take two parameters, Name and Location
# if we want to have more than one parameter, we can
# use comma to separate them.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")


greet_with("Manav", "Agra")

# What happens if we switch the order of the data that we give it.
# greet_with("Nowhere", "Jack Bauer")


# What happened here is, it takes the position of the data and
# looks at these arguments, and the first argument gets assigned
# to the first parameter. Second argument gets assigned to second
# parameter

## --- This is called a positional argument - This is the default way of calling a function

'''
even if we had more inputs 
def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    
    
my_function(1, 2, 3)


this means that 
a = 1 
b = 2 
c = 3

now if we switch around the arrangement of the in the function call

my_function(3, 1, 2)

a = 3 
b = 1
c = 2

# What if we want to be more clear when we actually call 
the function so we don't ever encounter this problem? 

# We can use keyword arguments instead 
'''
# What if we want to be more clear when we actually call
# the function so we don't ever encounter this problem?

# We can use keyword arguments instead
"""
def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    

# Instead of just adding the arguments into the function call
we can actually add each of the parameter names and an equal sign to say the 
a = 1, b = 2, c = 3 and if we change the order, it will still be the same.
my_function(a=1, b=2, c=3)
"""

# Calling the function using keyword arguments
greet_with(location="Nowhere", name="Jack Bauer")
