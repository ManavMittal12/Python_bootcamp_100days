# *args: Many positional arguments

# Unlimited Position Arguments
'''
def add(n1, n2):
    return n1 + n2

we can only add two values with this function.
'''

'''
what if we want to make our function more flexible and increase any number of arguments 

by convention, programmers use args, but we don't have to follow the convention,
but we do need the asterisk. This tells python that this function add can accept any number of arguments.
and once inside the function, we can loop through all the arguments which will be in the form of a tuple
and you can do whatever it is that you want with each of those arguments

def add(*args):
    for n in args:
        print(n)
        
        
add(3 , 5 , 6 , 8 , 2)
'''

# create a function add, where you pass any number as you want and add together
# all the numbers and return a sum.

def add(*args):
    num = 0
    for n in args:
        num += n
    return num


print(add(1, 2, 5, 7, 9))
