# What does it mean to be a framework

# Library vs Framework
# A framework is like a library, in the sense that there is a piece of code
# but there are differences as well.

# The main difference is
# for a library, you are in full control when you call a method from a library
# and the control is then returned.

# for a framework, the code never calls into a framework, instead the framework calls you.


# make sure your file name does not conflict with the name of the framework
# or the library in-fact.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'
