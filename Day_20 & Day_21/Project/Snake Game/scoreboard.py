from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()



    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", align=ALIGN, font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
