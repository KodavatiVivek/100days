from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = r.randint(-280, 280)
        y = r.randint(-280, 280)
        self.goto(x, y)



