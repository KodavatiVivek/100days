import random
import datetime as dt
import smtplib
from calendar import weekday

now=dt.datetime.now()
myemail = "workt3833@gmail.com"
password = "qctutytzqjbppurv"

day=now.weekday()

if day==0:
    with open("quotes.txt",'r') as file:
        quotes=file.readlines()
        quote=random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as new_connection:
        new_connection.starttls()
        new_connection.login(user=myemail, password=password)
        new_connection.sendmail(from_addr=myemail, to_addrs="vivekchowdary678@gmail.com",
                                msg=f"Subject:Motivation\n\n{quote}")