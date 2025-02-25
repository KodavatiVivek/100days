from data import data
from logo import logo,vs
import random as r

def names(name_set):
    name=name_set['name']
    follower_count=name_set['follower_count']
    ocupation=name_set['description']
    country=name_set['country']
    return (f"Name is {name} from {country} doing as {ocupation}")

def compare(guess,a,b):
    if a > b:
        return guess=="a"
    elif a == b:
        print(f"I don't we are stuck but you can play again since we came to end A:{a}  B:{b}\n")
        higherlower()
    else:
        return guess=="b"


def higherlower():
    score = 0
    game_continue = True
    compare_word = r.choice(data)
    while game_continue:
        print(logo)
        start_name=compare_word
        compare_word = r.choice(data)
        print(f"Compare A :{names(start_name)}")
        print(vs)
        print(f"Against B: {names(compare_word)}")
        if start_name==compare_word:
            compare_word=r.choice(data)

        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        print("\n" * 20)
        a_follower=start_name['follower_count']
        b_follower=compare_word['follower_count']

        final=compare(guess,a_follower,b_follower)

        if final:
            score+=1
            print(f"Ohh Your correct.Your score is :- {score}")
        else:
            print(f"You lose and your final score is {score}\n try to best this score next time you play\n")
            game_continue=False


want_to_play=input("Want to play Yes: Y and No: N").lower()
if want_to_play=="y":
    higherlower()
else:
    print("Feel free to comeback when your are confident enough\n")