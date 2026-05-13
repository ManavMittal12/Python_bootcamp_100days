# Functions with Input

# Functions are like this
'''
def my_function():
    do this
    then do this
    after that do this


calling the function
def my_function()
'''


def greet():
    print("Hello")
    print("How are you?")
    print("Isn't the weather nice?")


# It's going to do the same thing when we call greet
# greet()
# greet()


# But we want to modify the function such that there is variation
# in it.



'''
                123 function will receive this
def my_function(something):         <--- We can add the name of a variable in the paranthesis to start giving our functions some input.
    do this with something          <--- Do something with the something variable    
    then do this
    after that do this


calling the function
                123 If we send this
def my_function(data)   <--- data that we want to pass over to the function
'''

# It's like plugging the usb into computer. Like changing the input to the computer.


def greet_with_name(name):
    print(f"Hello {name}")
    print("How are you? {0}".format(name))


greet_with_name("Manav")
greet_with_name("Batman")

# We can create one function that carries out some instructions
# but everytime we execute it, we get to modify it a lil bit by
# changing the input

# Two things we are working with,
'''
def my_function(something):         # here we are basically doing something = 123, we are effectively creating a new variable and we are setting a new peice of data
                                    that we are passing 
    # Do this with something 
    # then do this 
    # Finally do this
    
In programming lingo we call this 
parameter = argument
something = 123

argument is the actual piece of data that will be passed over to the function when it's called upon
whereas the parameter is the name of that data, and we use the parameter inside the function to refer to it 
and do things with it.
'''
