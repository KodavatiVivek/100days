from distutils.dep_util import newer
from turtle import Turtle, Screen

from Demos.SystemParametersInfo import new_h
from nbformat.v3 import new_heading_cell

joe=Turtle()

def move_forward():
    joe.forward(10)

def move_backward():
    joe.backward(10)

def turn_left():
    new_heading=joe.heading()+10
    joe.setheading(new_heading)

    # joe.left(10)

def turn_right():
    new_heading=joe.heading()-10
    print(new_heading)
    joe.setheading(new_heading)

    # joe.right(10)

def clear():
    joe.clear()
    joe.penup()
    joe.home()
    joe.pendown()


screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=turn_right)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="z",fun=move_backward)
screen.onkey(key="c",fun=joe.clear)


screen.exitonclick()
