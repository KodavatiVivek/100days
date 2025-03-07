import turtle
from turtle import Turtle, Screen
import pandas as pd
import time
#from score import Score

screen = Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()

def get_mouse_click_coor(x, y):
    print(x, y)

def write_state_name(x, y, state_name):
    t=Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(state_name)

def missing(states):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write(f"Missing States :{states}" , align="center", font=("Courier", 12, "normal"))
    time.sleep(3)


guess=[]
#turtle.onscreenclick(get_mouse_click_coor)

while len(guess)<50:
    answer_state=screen.textinput(title=f"You have answered {len(guess)}/50 States Correct", prompt="Enter the state name").title()
    if answer_state=="Exit":
        missing_states = [state for state in all_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing(missing_states)
        missing_states_df.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guess.append(answer_state)
        state_data=data[data.state==answer_state]
        write_state_name(int(state_data.x), int(state_data.y), answer_state)
        all_states.remove(answer_state)






















