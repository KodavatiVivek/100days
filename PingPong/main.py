from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen=Screen()
screen.tracer(0)

paddle1=Paddle(350)
paddle2=Paddle(-350)
ball=Ball()
score=Score()




screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()


screen.onkeypress(paddle1.move_up,"Up")
screen.onkeypress(paddle1.move_down,"Down")
screen.onkeypress(paddle2.move_up,"w")
screen.onkeypress(paddle2.move_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.wallbounce()

    # Detect collision with paddles
    if ball.distance(paddle1)<50 and ball.xcor()>320:
        ball.paddlebounce()

    if ball.distance(paddle2)<50 and ball.xcor()<-320:
        ball.x_move*=-1

    if ball.xcor() > 380:
        ball.resetposition()
        ball.paddlebounce()
        score.lpoint()


    if ball.xcor() < -380:
        ball.resetposition()
        ball.paddlebounce()
        score.rpoint()

    if score.lscore==10 or score.rscore==10:
        if score.lscore>score.rscore:
            score.goto(0,0)
            score.write(f"Left Player Wins", align="center", font=("Courier", 24, "normal"))
        else:
            score.goto(0,0)
            score.write(f"Right Player Wins", align="center", font=("Courier", 24, "normal"))



screen.exitonclick()



