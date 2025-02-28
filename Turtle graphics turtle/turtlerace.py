from turtle import Turtle, Screen
import random as r
import time
color=["red","blue","green","yellow","orange","purple"]
screen=Screen()
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win Choose the color)")
screen.setup(width=500,height=400)
screen.bgcolor("lightblue")
y=-150
turtles=[]
for i in range(0,6):
    tim=Turtle("turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-230,y)
    y=tim.ycor()+50
    turtles.append(tim)

if user_bet:
    israce=True

while israce:
    for tur in turtles:
        x = tur.xcor()
        if x>230:
            israce=False
            wincolor=tur.pencolor()
            if wincolor==user_bet:
                print(f"you win the bet the {wincolor} turtle won")
            else:
                print(f"you lose the bet the {wincolor} turtle won")
        tur.forward(r.randint(1,10))
        time.sleep(0.1)

screen.exitonclick()
