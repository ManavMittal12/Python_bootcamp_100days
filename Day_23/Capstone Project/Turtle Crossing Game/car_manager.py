from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_a_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_x = 300
            random_y = random.randint(-250, 250)
            new_car.goto((random_x, random_y))
            self.cars_list.append(new_car)


    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.car_speed)


    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
