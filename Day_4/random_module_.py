'''
## Random Module

# Randomisation -->
# To create unpredictable behavior in computer

# Deterministic - Things that perform repeated action in a
# fully predictable way

# How to make them create random numbers?
# Computers can do pseudorandom number generator
# one that pyton uses is called
# Mersenne Twister


# Now it is very difficult for us to implement the mersenne twister
# and probably take us months to implement it.

# Python team has already created the random module
# has a bunch of functions that can help produce
# random int, float etc etc

# We have to import it first

https://docs.python.org/3/library/random.html
'''

import random

# we will use random.randint(a,b)
# generates number between a<= N <= b

# random refers to the module we imported which contains all the code
# then we use dot, and name of the function.


random_integer = random.randint(1, 10)
print(random_integer)

# Random is a python module
# What is a module ?
# We have been writting our code in the same page
# in a script style and everything being executed top to bottom

# sometimes code will become too long and difficult to
# understand in this large piece of code
# so people will split the code in individual module
# where each module will be responsible for different functionality in
# your program

# for complex project with many modules, there can be collaboration
# and different people working on different modules

# Random module was created my the python team.

# how can we make out own modules?
# we create a python file, do our task and can import it in
# other file (which is mostly the primary file.)
# we have to import it using import keyword
import my_module
print(my_module.my_fav_number)  # same as we say for random module


# ----------------------------------------
# Generating random floating point numbers
random_number_0_to_1 = random.random()  # This doesn't take any input
print(round(random_number_0_to_1, 2))
# some functions don't take any input at all but still take paranthesis
random_number_0_to_1 = random.random() * 10  # This doesn't take any input
print(round(random_number_0_to_1, 2))


# There's another function for random floating point generator
# random.uniform(a, b)
# a <=- N <= b
random_float_number = random.uniform(1, 10)
print(random_float_number)

# Recommended to use random.random number.
