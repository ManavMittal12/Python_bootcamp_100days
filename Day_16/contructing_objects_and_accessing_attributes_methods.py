# Constructing objects and accessing their attributes and methods

# A car's blueprint
# color of the car
# wheels it should have
# mileage
# fuel it has
# all of this data with functionality
# ability to start, stop etc.
# all of this combined is a blueprint of the class

# we can then create objects from this.
# the object is the actual thing that we're going to be using in our code.


# creating a new object from a blueprint looks like
# car = CarBlueprint()
# object     class      # object is created from this car blueprint

# classes are normally written with the first letter of each word capitalized,
# which is known as pascal case. This is to differentiate it from all the variable and function
# names that we give in python. where each word is separated by underscores.
# in python


# All we have to do to create the object from the class is to give the object a
# name set it equal to the name of the class and the parenthesis
# parentheses like function activates the construction of this object from the blueprint


# we are going to use a library to practice it
# for example, someone creates a blueprint of a turtle with a paintbrush
# we can tell the turtle to have diff colors and draw etc

# library name is turtle graphics.
import turtle       # blueprint is in turtle module

# tapping into the class turtle
timmy = turtle.Turtle()   # from turtle module, Turtle class and parentheses to construct an object
# It creates a turtle object
print(timmy)    # when you print this object, it returns the object <turtle.Turtle object at 0x00000205D3AAB770> Nothing useful

'''
or you can do
from turtle import Turtle
timmy = Turtle()
'''

# object attributes
# It has certain attributes

# when we want to access these objects, syntax looks like this
# car.speed (dot separates the object with the attributes )
# this code basically identifies the object, and then it says, from object
# get the speed attribute.

timmy.color("black")
timmy.shape("turtle")


# my_screen = turtle.Screen() # Accessing the screen class in the turtle module
# print(my_screen.canvheight) # Opens the screen for a moment and prints screen height.


# object methods
# Things that it can do
# functions tied to those objects - methods
# syntax
# first we will tap into call objects, then we'll use the function associated with the object, which is called methods
# my_screen.exitonclick() # will allow our program to continue running until we click on the screen.
# our error is our turtle.


# there are other methods as well
# timmy.color("brown3")  # check the documentation for more.
# timmy.shape("turtle")

# challenge, make the turtle move 100 paces.

timmy.forward(100)

my_screen = turtle.Screen()

my_screen.exitonclick()
