from turtle import Screen
from ping_board import Paddle


screen = Screen()
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

f_paddle = Paddle(x_pos=350)
s_paddle = Paddle(x_pos=-350)


screen.onkey(key="Up", fun=f_paddle.up)
screen.onkey(key="Down", fun=f_paddle.down)


game_on = True
while game_on:
    screen.update()



screen.exitonclick()
