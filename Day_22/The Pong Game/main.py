from turtle import Screen
from ping_board import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

r_paddle = Paddle(x_pos=350)
l_paddle = Paddle(x_pos=-350)

ball = Ball()


screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_on = True
while game_on:
    time.sleep(.1)
    screen.update()


    ball.move_ball()



screen.exitonclick()
