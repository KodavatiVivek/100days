import random as r

from logo import logo

def guess_number():
    return r.randint(1,100)

def check(user_input, guess_num,turns):
    if user_input > guess_num:
        print(f"You have to try lower number than {user_input}")
        return turns - 1
    elif user_input< guess_num:
        print(f"You have to try Higher number than {user_input}")
        return turns - 1
    elif user_input==guess_num:
        print(f"You Won! . The number is {guess_num}")

def lifes(level):
    if level =='hard':
        return 5
    elif level =='easy':
        return 10

def guessthenumber():
    life = lifes(input("Choose a difficulty. Type 'easy' or 'hard':").lower())
    correct_guess = guess_number()
    User_guess=0
    while User_guess!=correct_guess:
        print(f"You have only {life} left before you die\n")
        user_guess = int(input("Enter your guess to find the answer\n"))
        life=check(user_guess, correct_guess,life)

        if life == 0:
            print("You've run out of guesses, you lose.")
            return
        elif User_guess != correct_guess:
            print("Guess again.")
pl= True
while pl:
    play = input("want to play. Type 'yes' or 'no:").lower()
    if play == "yes":
        print("\n" * 20)
        print(logo)
        print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
        guessthenumber()
    else:
        print("What happened are you scared\n")
        pl= False