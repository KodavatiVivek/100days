from tkinter import *
from tkinter import messagebox
import Generator
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Gen():
    password=Generator.password()
    pass_ok=messagebox.askokcancel(title="Generated Password",
                                       message=f"your generated password is {password} ")
    if pass_ok:
        input_passw.insert(0, f"{password}")
        pyperclip.copy(password)

        #_---------------------------------#

def search():
    website_name=input_website  .get()
    try:
        with open("data.json", "r") as file:
            # reading the data
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("data.json", "w") as file:
            messagebox.showinfo(title="Error", message="No Data File Found.")
    if website_name in data:
        email = data[website_name]["Email"]
        print(email)
        password = data[website_name]["Password"]
        messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website_name} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #



def save():
    Email = input_email.get()
    Pass = input_passw.get()
    website = input_website.get()

    new_data={
        website:{
            "Email":Email,
            "Password":Pass
        }
    }

    new_data1 = {
        "Email": Email,
        "Password": Pass
    }

    if len(website)==0 or len(Pass) == 0:
        messagebox.showinfo(title="OOPS", message=f"You have left website and Password fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # reading the data
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data={}
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data,file,indent=4)
        else:
            data.update(new_data)
            #writing the data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            input_website.delete(0, END)
            input_passw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Your Password Manager")
window.config(pady=50,padx=50,bg="light green")

canvas=Canvas(width=200,height=200,bg="light green",highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

Lwebsite=Label(text="Website:",bg="light green", font=("Ariel",10,"bold"))
Lwebsite.grid(column=0,row=1)

Email=Label(text="Email/Username:",bg="light green",font=("Ariel",10,"bold"))
Email.grid(column=0,row=2)
passw=Label(text="Password:",bg="light green",font=("Ariel",10,"bold"))
passw.grid(column=0,row=3)


input_website = Entry(width=20,bg="light green")
input_website.grid(column=1,row=1)

input_email= Entry(width=38,bg="light green")
input_email.grid(column=1,row=2,columnspan=2)
input_email.insert(0,string="Janedoe@gmail.com")

input_passw= Entry(bg="light green")
input_passw.grid(column=1,row=3)

Gener_button=Button(text="Generate Password",bg="light green",highlightthickness=0,command=Gen)
Gener_button.grid(column=2,row=3)

Add_button=Button(text="ADD",fg="Blue",bg="light green",highlightthickness=0,width=36,command=save)
Add_button.grid(column=1,row=4,columnspan=2)

Search=Button(text="Search",bg="light green",highlightthickness=0,command=search)
Search.grid(column=2,row=1)

































window.mainloop()