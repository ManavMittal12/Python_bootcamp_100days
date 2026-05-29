from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(10)



def move_backward():
    tom.backward(10)


def turn_left():
    tom.left(10)


def turn_right():
    tom.right(10)


def clear_screen():
    tom.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
