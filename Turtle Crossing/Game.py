from turtle import Screen
from PlayerTurtle import Player
from Car import Car
from Score import Scoreboard
import random as r
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)

car=Car()
car.hideturtle()
player=Player()
score= Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

is_gameon=True
while is_gameon:
    time.sleep(0.1)
    screen.update()
    car.new_cars()
    car.move()
    if player.ycor() > 280:
        player.reset()
        score.increase_score()
        car.level_up()
        screen.bgcolor(r.choice(["black", "white","brown"]))

    for cars in car.cars:
        if cars.distance(player) < 25:
            is_gameon = False
            score.game_over()
            break













screen.exitonclick()
