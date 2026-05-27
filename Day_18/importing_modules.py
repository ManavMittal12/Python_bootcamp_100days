# Importing modules, installing packages, and working with Aliases.
import random
# import Module_name
import turtle

# to create a new turtle object
tim = turtle.Turtle()

# we can also write the import like this
# keyword from, module name, keyword import, Thing in the module
from turtle import Turtle

# with this kind of syntax, we can simply write
tom = Turtle()  # we don't have to keep writing turtle.Turtle()


# we can also use this
# from keyword, module name, import keyword, (*) asterisk sign to show that we want to import everything
from turtle import *        # Though, it's unusual in python community to write the code like this.
# now we can use everything in the module like it is in our current file.
# it can make hard for us to figure out where the classes or methods came from.

# eg
forward(100)


# Aliasing the methods

# keyword, module_name, keyword, alias_name
import random as r

n = 12
r.randint(n, 100)



# There are some modules that you can't just import
# we can check modules in pypi

# eg
import heroes   # module name is not available.

# this module is not present in the python standard library
# it's a very small library.

# pypi is a bigger library, we can check the modules from there,
# and then we can install that module in our environment.
print(heroes.gen())


# when you try to import something that is not installed, it will give us error.
# remember that when you install a module, and it's not bundled in the py standard library,
# we have to install it

# when we install a package, it gets installed in a python virtual environment
# which is per-project basis.

# inside the site-packages.

# virtual environment and packages get installed in the projects we are making.


# python 3 is not backward compatible with python .

# we can also install packages using pip
