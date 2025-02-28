import time
from turtle import Turtle
import random as r
import time

start = 5
increment = 5
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars =[]
        self.start = start

    def move(self):
        for car in self.cars:
            car.backward(self.start)


    def new_cars(self):
        if r.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.color(r.choice(["red", "orange", "yellow", "green", "blue", "purple"]))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, r.randint(-250, 250))
            self.cars.append(car)

    def level_up(self):
        self.start += increment
        for car in self.cars:
            car.backward(self.start)
        self.new_cars()

