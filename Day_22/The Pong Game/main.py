from turtle import Screen
from ping_board import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title(titlestring="Pong Game")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

r_paddle = Paddle(x_pos=350)
l_paddle = Paddle(x_pos=-350)

ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with the paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.deflect()


    # if R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # if L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
