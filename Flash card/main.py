import pandas
import pandas as pd
import random as r
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("./data/french_words.csv")
    dictionary = df.to_dict(orient="records")
else:
    dictionary = df.to_dict(orient="records")



def next():
    global current_card,time
    window.after_cancel(time)
    current_card = r.choice(dictionary)
    canvas.itemconfig(card_image, image=front)
    canvas.itemconfig(text, text="French",fill="black")
    canvas.itemconfig(current, text=current_card["French"],fill="black")
    time=window.after(3000, flip)

def flip():
    canvas.itemconfig(card_image, image=back)
    canvas.itemconfig(text, text="English",fill="white")
    canvas.itemconfig(current, text=current_card["English"],fill="white")

def is_known():
    dictionary.remove(current_card)
    data=pandas.DataFrame(dictionary)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next()


window = Tk()
window.title("Flash cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

time=window.after(3000, flip)

front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 270, image=front)
text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
current = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

correct = Button(window, image=right, command=is_known, highlightthickness=0, padx=50, pady=50)
correct.grid(row=1, column=0)

wrong = Button(window, image=wrong_image, command=next, highlightthickness=0, padx=50, pady=50)
wrong.grid(row=1, column=1)

next()  # Start the first card
window.mainloop()