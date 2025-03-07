from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()


def update_score():
    self.write(f"Score: {self.score} High score :{self.high_score}", align="right", font=("Courier", 12, "normal"))


def increase_score():
    self.score += 1
    self.clear()
    self.update_score()