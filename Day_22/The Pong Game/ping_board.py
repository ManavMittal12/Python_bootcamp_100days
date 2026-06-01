from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_pos, y=0)



    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
