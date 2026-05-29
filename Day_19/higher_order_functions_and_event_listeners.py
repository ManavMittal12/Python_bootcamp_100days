# Turtle Event Listeners
from turtle import Turtle, Screen

thomas = Turtle()
screen = Screen()


# we grab a screen object, and tell it to start listening
screen.listen()

# to bind a keystroke to an even, we use listen() function


# this is the function, it is going to make the turtle object go forward
def move_forward():
    thomas.forward(10)


# this is an even listener. Binding a function to this method
screen.onkey(key="space", fun=move_forward)
# key = space, we are telling it, that when the space key is pressed, we
# want the function "move_forward to be triggered"

# important point, when we use a function as an argument, we don't add the
# parenthesis at the end, the parenthesis triggers the function.
# but what we want is we want this method, onkey, to listen for
# when the space bar is pressed and only when that happens, to trigger the
# "move_forward" function

screen.exitonclick()



# Function as input
# What we saw here is function as input,

'''
for example, 
we have a function 

def function_a(something):
    # Do this with something
    # then do this
    # finally do this
    
    
def function_b():
    # Do this
    
    
we can pass function b to function a like this
function_a(function_b)

we pass only the name when we pass a function as an input 
'''

'''
# Understanding how it works with calculator example
def add(n1, n2):
    return n1 + n2
    
    
def sub(n1, n2):
    return n1 - n2
    
    
def mul(n1, n2):
    return n1 * n2
    
    
def divide(n1, n2):
    return n1 / n2
    

def calculator(n1, n2, func):
    return func(n1 , n2)
    
    
calling the function
result = calculator(2, 3, divide)
print(result)
'''

'''
Higher Order Function

the idea of a higher order function is a function that 
can work with other functions. 

in above case, calculator() function is the higher order function.
'''


# Recommendation
# when you're using methods, that you haven't created yourself,
# like onkey above, use keyword arguments instead of positional arguments.
