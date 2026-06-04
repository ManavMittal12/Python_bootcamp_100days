from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as self.high_score_data:
            self.high_score = int(self.high_score_data.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)


    def update_score(self):
        self.score += 1
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as self.high_score_data:
                self.high_score_data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
