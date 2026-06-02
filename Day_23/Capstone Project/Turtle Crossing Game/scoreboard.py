from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.current_level = 0
        self.goto(x=-210, y=250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level {self.current_level}", align="Center", font=FONT)

    def increment_score(self):
        self.current_level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align="Center", font=FONT)
