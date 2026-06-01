from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__(shape="circle")
        self.color("red")
        self.penup()


    def move_ball(self):
        x_cor = self.xcor() + 10
        y_cor = self.ycor() + 10
        self.goto(x_cor, y_cor)
