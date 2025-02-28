from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(pos,0)

    def move_up(self):
        new_y=self.ycor()+30
        self.goto(self.xcor(),new_y)
        if self.ycor()>250:
            self.goto(self.xcor(),250)

    def move_down(self):
        new_y=self.ycor()-30
        self.goto(self.xcor(),new_y)
        if self.ycor()<-250:
            self.goto(self.xcor(),-250)




