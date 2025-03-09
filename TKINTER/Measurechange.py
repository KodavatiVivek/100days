from tkinter import *

window = Tk()
window.title("Change Miles to KM")

window.minsize(width=500, height=300)
window.config(padx=10 ,pady=20)

def convert():
    km=(int(input_miles.get()) * 1.609).__round__(2)
    Km_result.config(text=f"{km}")


input_miles = Entry(width=6)
input_miles.grid(column=1, row=0)

miles_label=Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

isqual=Label(text="equal to", font=("Arial", 12))
isqual.grid(column=0, row=1)

Km_label=Label(text="KM", font=("Arial", 12))
Km_label.grid(column=2, row=1)


Km_result=Label(text="0")
Km_result.grid(column=1,row=1)


button=Button(text="calculate",command=convert)
button.grid(column=1,row=2)












































window.mainloop()