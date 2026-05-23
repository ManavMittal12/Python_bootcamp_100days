# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("You got it")

def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")
# so try to describe your problem to better debug.

my_function()

# Describe the Problem - Write your answer as comments:
# 1. What is the for loop doing?
# The for loop here is using the range function to
# iterate from 1 to 20(upto but not including)

# 2. When is the function meant to print "You got it" ?
# Function is meant to print when `i` reaches 20

# 3. What are your assumptions about the value of `i` ?
# the assumption is that we will reach 20.
# `i` will never reach 20, because in range function, it's upto but not including.
