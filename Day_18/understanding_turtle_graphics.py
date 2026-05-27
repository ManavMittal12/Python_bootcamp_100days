# Turtle Module - is a graphics module

# Turtle module can help us create graphics on screen

from turtle import Turtle, Screen

def turn_left_move():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("BlueViolet")

for _ in range(4):
    turn_left_move()


# Keeping this at the very end.
# The way the programmers go about knowing how to use a module is
# using the documentation

# Documentations are really long, Go to the contents page, and you'll
# know what you can do with the turtle.

# Very often, we might need the help of stack overflow.

screen = Screen()
screen.exitonclick()


# What is tk module ? tkinter? -- It is a module that we can use in python
# to create a graphic user interface (GUI).

# Turtle module relies on tkinter to create the graphics that it does.


# In pycharm or intellij, we can refactor our code names
