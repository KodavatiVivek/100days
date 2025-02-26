import random as r
print("Who wants to Pay the Bill. Please put your rich cards out\n")

members=int(input("Please state how many members"))
Friends=[]
for i in range(members):
    Friends.append(input("enter your names"))

Popb= r.choice(Friends)
print(f"Your are busted mann {Popb}")
Pot=r.randint(0,members-1)
print(f"Tip is important please {Friends[Pot]}")