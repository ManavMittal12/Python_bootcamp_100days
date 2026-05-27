# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

from turtle import Turtle, Screen
from random import choice


tim = Turtle()

# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.42)
#
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(choice(colors))
    draw_shapes(shape_side_n)
screen = Screen()
screen.exitonclick()
