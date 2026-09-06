# Python Decorators
import time
# functions can have functionality/input/output
# functions are first class objects and can be passed as arguments
# functions can be nested in another functions.
# functions can be returned as the output from another functions.

# Creating a python Decorator

# first we create a normal function. This function is going to
# take another function as input.
"""def decorator_function(function):
    # inside this decorator function, we are going to create a wrapper function
    def wrapper_function():
        # this wrapper function is then going to execute the function
        # that was passed in as an argument in the decorator function.
        
        # This is a nice way of adding something that you could do
        # before running the function
        function()
        # at the end of calling all the lines in our decorator_function
        # we are going to return out wrapper_function but without the parenthesis.

        # Do something after the function.
        # or maybe if we wanna run the function twice, we can do that.
        
        
    return wrapper_function"""


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function

# basically what we have done is, we've created a decorator_function,
# which can do some stuff, and it could control the calling of the function,
# that was passed in.

# Remember, decorator function is just a function that wraps another
# function and gives that function some additional functionality.

# what if we want to add a delay, we can do it in this function, but what if
# there are a lot of functions, and we want to do the same thing, then it
# will be repetitive. That's where decorators come it.


# use the @ symbol, and the "delay_decorator" which we want to delay.
@delay_decorator
def say_hello():
    print("Hello!")
# what if I don't want to run this immediately the moment I run the script.
# and add a delay to this function.
# we can add the same decorator in front of all three functions.


@delay_decorator
def say_bye():
    print("Bye!")



def say_greeting():
    print("Greetings!")


# now when we run our function, it will run with extra functionality.
say_hello()


# These "@" signs are called Syntactic Sugar. It's some syntax that you can write
# to make it easier to write an alternative line of code.

# what if we wanted to add the decorator to this greeting, if instead of using
# this syntactic sugar with the @ sign, we could just call the name of the decorator and pass in the name
# of our function, and we will end up with the decorated function with the output of our function

decorated_function = delay_decorator(say_greeting)
decorated_function()



# In flask, we saw
# @app.route("/")
# we saw that this is a decorator
# it's making sure, that it triggers a particular function
# when the user wants to access homepage using "/".
