import turtle
import random





def select_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tom = turtle.Turtle()
turtle.colormode(255)
tom.speed("fastest")
tom.setheading(tom.heading() + 10)


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tom.pencolor(select_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(2)


screen = turtle.Screen()
screen.exitonclick()
