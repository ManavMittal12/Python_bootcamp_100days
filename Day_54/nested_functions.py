# Nested Functions

# Functions can also be nested inside other functions

# eg
"""
def outer_function():
    print("I'm Outer")

    # Now we have the issue of calling this function, since it's scope
    # is local to the "outer_function".
    def nested_function():
        print("I'm Inner")

    # Calling the "nested_function" inside the "outer_function" will run
    # just fine.
    nested_function()
"""
# If we try to call the "nested_function" from top level, it will give
# name error, because it's local to the outer_function.
"""nested_function()   # Unresolved reference 'nested_function'"""


# outer_function()


# one of the things we can do is to return a function from another function.
# Functions can be returned from other functions.
def outer_function():
    print("I'm Outer")

    def nested_function():
        print("I'm Inner")

    # instead of calling the nested_function, we are returning it ("Without the parenthesis.")
    return nested_function


# Now if we call the outer function, the output this value is going to evaluate
# to is going to become the nested function.

# so, we equal to the output of the outer_function(), which is this nested function
# being returned. Well then, not only can we return the outer function, which is going to give me outer,
# now, I can also trigger the inner_function separately by calling it and then adding the activator(i.e. parenthesis.)
outer_function()
print("outer triggered only.")
inner_function = outer_function()
inner_function()
