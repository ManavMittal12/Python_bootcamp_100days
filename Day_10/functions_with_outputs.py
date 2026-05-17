# Functions with outputs

# we have already seen the couple of things in functions.
# Normal functions
# passing the parameters in functions

# Now, we'll see the final flavor of functions, the functions
# that allows us to have output from a functions

'''
def my_function():
    results = 3 * 2 # Calculates this and saves to a variable
    return results   # Then we can use the 'return' keyword to output whatever it is we want to be the output of this function.
    # the output is the result

output = my_function()  # Output will store the returned value from the function.
if we call the function and later output this result, and it runs, it will go ahead and output the result by replacing the
code which is calling the function. We have to save it in another variable

# Functions are like machines
# in goes empty bottles
# after some process, a bottle comes out with milk.
# so that function has the input as empty bottles
# and the output is the glass bottles filled with milk.
# in the middle, there's some processes or some code that's being executed to
# create this change.
'''

# example

def format_name(fname, lname):
     fname = fname.capitalize()
     lname = lname.capitalize()
     return f"{fname} {lname}"  # This formatted string becomes the value we are returning to the function call


f_name = "baTMan"
l_name = "wayNE"
output = format_name(f_name, l_name)
print(output)

# or we can

print(format_name(f_name, l_name))


# we have been using who have their functionality predetermined, and we
# haven't created it.

# eg
output_new = len("Angela")  # This return function returns the length of the string
print(output_new)

# What is the difference between print statement and output in the function itself?
# what if we create a function and it does things differently

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

# neither of these functions have print statements

output = function_1("hello")
print(output)   # we have output from one function.

# What if, we take the output of function one and use it as input for function two
# we can do that now

output2 = function_2(output)
# or
output3 = function_2(function_1("ayooooo"))
print(output3)
