from turtle import Turtle, Screen
import random as r
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head= self.snake[0]

    def create_snake(self):
        x = r.randint(-200,200)  # start x at 0
        for i in range(0, 3):
            self.add_segment((x, 0))
            x -= 20

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]


    def move(self):
        for sn in range(len(self.snake) - 1, 0, -1):
            x = self.snake[sn - 1].xcor()
            y = self.snake[sn - 1].ycor()
            self.snake[sn].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake.append(t)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)







