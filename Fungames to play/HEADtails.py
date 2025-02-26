import random as r
print(" Welcome to toss choose heads or tails\n")

c=input("Heads or Tails")
f=r.randint(0,1)

if f==0:
    a="Heads"
else:
    a="Tails"

if a==c:
    print("You Won")

