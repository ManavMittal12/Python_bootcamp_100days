# Setting default value for optional arguments in function header

# Advanced Arguments (Advance python arguments)

'''
we know how keyword arguments work

def my_function(a, b, c):
    # Do this with a
    # then do this with b
    # Finally do this with c


my_function(a=1, b=2, c=3)

we have to put values everytime for a, b and c.
'''

# Python has a neat way of solving this by creating arguments
# that have default values.

# we can do that by changing function definition.
'''
we can give the function some values to start off with
def my_function(a=1, b=2, c=3):
    # Do this with a
    # then do this with b
    # Finally do this with c
    
    
my_function()

# if we want to give custom values, we can do
my_function(a=10, b=2, c=4)
'''
