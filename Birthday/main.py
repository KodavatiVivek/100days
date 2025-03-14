import smtplib
import datetime as dt
import pandas as pd
import random
import os


myemail="workt3833@gmail.com"
password="qctutytzqjbppurv"

dates=pd.read_csv("birthdays.csv")
birtharray=dates.to_dict(orient="records")
now=dt.datetime.now()
month=now.month
day=now.day

for person in birtharray:
    date=dt.datetime(year=person["year"],month=person["month"],day=person["day"])
    if month == date.month and day == date.day:
        with open("quotes.txt", 'r') as file:
            quotes = file.readlines()
            quote = random.choice(quotes)

        letter_templates = [f for f in os.listdir("letter_templates") if f.startswith("letter_")]
        selected_template = random.choice(letter_templates)

        with open(f"letter_templates/{selected_template}","r") as file:
            letter=file.read()
            letter=letter.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as new_connection:
            new_connection.starttls()
            new_connection.login(user=myemail, password=password)
            new_connection.sendmail(from_addr=myemail, to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday\n\n {letter}\n\n{quote}")



