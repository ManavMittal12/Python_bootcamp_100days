import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
screen.onkey(key="Up", fun=turtle.move_up)

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    cars.create_a_car()
    cars.move_cars()

    # detect collision with car
    for car in cars.cars_list:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


    if turtle.check_finish_line() is True:
        scoreboard.increment_score()
        turtle.reset_position()
        cars.increase_speed()


screen.exitonclick()
