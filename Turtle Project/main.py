import turtle
from turtle import *
from turtle import Turtle, Screen
import random as r
import numpy as np
import heroes as h

vivek= Turtle()
screen=Screen()
turtle.colormode(255)
vivek.shape("turtle")
vivek.dot(2)
def number_of_sides(sides):
    for i in range(3, sides):
        random_color = tuple(np.random.choice(range(256), size=3))
        for j in range(i):
            vivek.forward(100)
            vivek.right(360 / i)
            vivek.color(random_color)
            vivek.speed(10000000)

def path():
    while True:
        vivek.pensize(5)
        vivek.forward(10)
        random_color = tuple(np.random.choice(range(256), size=3))
        vivek.right(r.choice([0,90,180,270]))
        vivek.left(r.choice([0, 90, 180, 270]))
        vivek.color(random_color)
        vivek.speed("fastest")

def circle():
    for i in range(1,180):
        random_color = tuple(np.random.choice(range(256), size=3))
        vivek.color(random_color)
        vivek.circle(100)
        vivek.setheading(i)
        vivek.speed("fastest")

def circle_spirograph(size_of_gap):
    for i in range(360//size_of_gap):
        random_color = tuple(np.random.choice(range(256), size=3))
        vivek.color(random_color)
        vivek.circle(100)
        vivek.setheading(vivek.heading()+size_of_gap)
        vivek.speed("fastest")


circle_spirograph(1)
my_screen = Screen()
my_screen.exitonclick()