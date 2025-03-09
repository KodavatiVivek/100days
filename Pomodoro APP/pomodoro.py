from itertools import count
from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkmark='✓'
reps=0
Checks=""
timer_main=None

window=Tk()
window.title("POMODORO TIMER")
window.config(bg=YELLOW,padx=100,pady=100)

def timestart():
    global reps,Checks
    reps+=1

    if reps%8==0:
        timer(LONG_BREAK_MIN*60)
        Timer.config(text="LONG BRWAK",fg=PINK)
    elif reps%2==0:
        timer(SHORT_BREAK_MIN*60)
        Timer.config(text="SHORTBREAK", fg="Purple")
    else:
        timer(WORK_MIN*60)
        Timer.config(text="WORKTIME", fg="red")
        Checks += checkmark
        check_marks.config(text=Checks)



def reset():
    window.after_cancel(timer_main)
    canvas.itemconfig(Timetext, text="00:00")
    Timer.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


def timer(count):

    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(Timetext, text=f"{minutes:02d}:{seconds:02d}")
    if count>0:
        global timer_main
        timer_main=window.after(1000,timer,count-1)
    else:
        timestart()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


Timer=Label(text="TIMER",fg="darkgreen",bg=YELLOW,font=(FONT_NAME,50))
Timer.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
Timetext=canvas.create_text(100,112,text="00:00",fill="White",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)


Start_Button=Button(text="START",fg="Blue",bg=YELLOW,command=timestart,font=(FONT_NAME,10),highlightthickness=0).grid(column=0,row=2)
Reset_Button=Button(text="RESET",fg="Blue",bg=YELLOW,command=reset,font=(FONT_NAME,10,'bold')).grid(column=2,row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

































window.mainloop()
