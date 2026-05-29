import turtle
from turtle import Turtle, Screen
import random

# Building the turtle race project


screen = Screen()

# To change the screen size.
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles_list = []
x_axis = -230
y_axis = -100


for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x_axis, y_axis)
    y_axis += 40
    turtles_list.append(new_turtle)

'''
# it takes an attribute.
# using the .goto to define the x and y value.
# imagine program window as a graph
# if it has a height of 400, it has a y-axis, it goes till 200 upwards and -200 downwards
# similarly, if we have a width of 500, it has x-axis which goes from 250 towards right and -250 towards left
# and the current axis is (0, 0)
# tim.penup()
# tim.goto(x=-230, y=-100)
'''

# get the turtles to start moving.
is_race_on = True
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
