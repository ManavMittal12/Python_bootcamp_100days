from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)


    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False


    def reset_position(self):
        self.goto(0, -280)
