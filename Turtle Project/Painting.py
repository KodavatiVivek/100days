import turtle
from turtle import *
from turtle import Turtle, Screen
from color import rgb_colors
import random as r
import numpy as np

vivek= Turtle()
screen=Screen()
turtle.colormode(255)
vivek.shape("turtle")
vivek.hideturtle()

numbers_c =int(input("Enter the number of dots you want to draw: "))

for dot_count in range(1,numbers_c+1):
    vivek.dot(20, rgb_colors[r.randint(0, 29)])
    vivek.penup()
    vivek.forward(50)

    if dot_count %10 == 0:
        vivek.setheading(90)
        vivek.forward(50)
        vivek.setheading(180)
        vivek.forward(500)
        vivek.setheading(0)






screen.exitonclick()