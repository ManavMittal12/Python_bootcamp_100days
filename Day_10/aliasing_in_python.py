
# Aliasing in python
# We can store a function as a value of a variable.
def add(n1, n2):
    return n1 + n2

# we trigger a function using parenthesis, if we write add()
my_fav_operation = add
# but if we want to store a function with another name
# , give it another reference, then we would do it like this without the parentheses, only
# with the name of the function.

my_fav_operation(2 , 3)
