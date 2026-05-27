# generate a random walk

# draw a random walk
# turtle can make random movements in north-east south of west
# color pallet changes in every walk
# get the thickness to change and increase the thickness
# and speed up the turtle

import random
from turtle import Turtle, Screen


tom = Turtle()
colors = ("CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen")
directions = (0, 90, 180, 270)
tom.width(15)
tom.speed("fastest")
tom.shape("turtle")

for _ in range(200):
    tom.forward(30)
    tom.color(random.choice(colors))
    tom.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
