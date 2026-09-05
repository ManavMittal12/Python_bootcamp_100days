from flask import Flask


app = Flask(__name__)


# "/" is the home route. Like when we go to www.google.com, "/" means
# that we want to see the homepage.

# that's what we are saying, that when the user wants to navigate to our
# homepage with just a forward slash, they want to see the homepage, so we're
# going to show them "hello world."

# this syntax is called a python decorator.
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
"""

# Python Decorator
# what is a python Decorators?

# let's imagine you have a bunch of function in class or module, and
# you want to add some functionality to each of these functions, you
# might use a decorator function to do that.

# you can think of them as a function, that's going to give additional functionality to
# an existing function.


# Functions inputs/Functionality/Output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# One of the things about python functions is that
# they are known as First-Class objects, can be passed aroun as arguments
# e.g. int/string/float etc.

# that means, we can take these functions, and we can build another function
# that uses these functions.


# now, when we call the calculate function,
# we give it the name of the functions from above and give it some numbers
# those numbers are going to become the input of that specified function,
# and then we are going to return the results of that function.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


# calling the calculate function and then passing a function as higher
# order function
result = calculate(add, 5, 2)
result2 = calculate(multiply, 5, 2)
print(result)
print(result2)

# The ability for us to treat functions as first-class objects basically means
# that we can pass them around as if they are any other argument, and later we
# can activate them by adding the parenthesis around.
