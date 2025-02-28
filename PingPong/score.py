from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rscore = 0
        self.lscore = 0
        self.goto(-100, 270)
        self.write(f"Score: {self.lscore}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 270)
        self.write(f"Score: {self.rscore}", align="center", font=("Courier", 24, "normal"))



    def update_score(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.lscore}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 270)
        self.write(f"Score: {self.rscore}", align="center", font=("Courier", 24, "normal"))

    def lpoint(self):
        self.lscore+=1
        self.update_score()

    def rpoint(self):
        self.rscore+=1
        self.update_score()
