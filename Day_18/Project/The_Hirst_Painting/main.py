from operator import pos

import colorgram as cg
import turtle as t
import random


# Used this to get a color list from a photo.
# def extract_rgb(image_name, no_of_colors):
#     img_colors = cg.extract(image_name, no_of_colors)
#     rgb_colors = []
#     for img_color in img_colors:
#         r = img_color.rgb.r
#         g = img_color.rgb.g
#         b = img_color.rgb.b
#         rgb_colors.append((r, g, b))
#
#     return tuple(rgb_colors)
#
#
# extracted_rgb = extract_rgb('hirst_painting_.jpg', 30)
# print(extracted_rgb)

def create_art():
    for _ in range(10):
        hirst_turtle.dot(20, random.choice(color_list))
        hirst_turtle.penup()
        hirst_turtle.forward(50)
        hirst_turtle.pendown()


color_list = ((31, 83, 183), (166, 10, 42), (180, 164, 30), (82, 103, 211), (220, 64, 118), (215, 132, 177),
              (134, 147, 214), (217, 160, 73), (84, 7, 34), (165, 52, 102), (31, 52, 145), (214, 221, 241),
              (231, 163, 196), (157, 92, 43), (236, 204, 66), (232, 201, 224), (174, 171, 235), (80, 4, 2),
              (234, 222, 197), (75, 118, 85), (224, 78, 55), (159, 11, 7), (32, 32, 85), (221, 236, 228),
              (139, 168, 144), (100, 149, 96), (234, 207, 11), (237, 165, 157), (91, 88, 12), (34, 84, 62))

# Use turtle
# paint a painting  with a 10 by 10 rows of spots
# dots should be 20 in size
# and spaces around with 50 paces

t.colormode(255)
hirst_turtle = t.Turtle()
DOT_SIZE = 20
DOT_SPACES = 50
hirst_turtle.speed("fastest")

hirst_turtle.setheading(225)
hirst_turtle.penup()
hirst_turtle.forward(250)
hirst_turtle.setheading(0)
hirst_turtle.pendown()
hirst_turtle.hideturtle()


for dot in range(10):


        create_art()
        hirst_turtle.setheading(90)
        hirst_turtle.penup()
        hirst_turtle.forward(50)
        hirst_turtle.setheading(180)
        hirst_turtle.forward(500)
        hirst_turtle.setheading(0)





hirst_painting = t.Screen()
hirst_painting.exitonclick()
