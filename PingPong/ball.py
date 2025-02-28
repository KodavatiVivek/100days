from turtle import Turtle
import random as r

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def wallbounce(self):
        self.y_move*=-1


    def paddlebounce(self):
        self.x_move*=-1
        self.movespeed *= 0.9

    def resetposition(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.paddlebounce()


