import random as r

from intake.source.cache import display
from sympy.concrete.guess import guess

from arthang import stages,logo
from Words import word_list

print(f"I have chosen a word try to guess it in 6 chances\n If not you will be HANGED{stages[0]} \n Think Carefully")
chosen_word=r.choice(word_list)

placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print("         ")
print(placeholder)
print("         ")

lives=6
game_over= False
correct=[]
while not game_over:
    print(f" *************************--You have only {lives} lives left -----------***********************8")
    guess= input("Please guess the letter\n").lower()
    display = ""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct.append(guess)
        elif letter in correct:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in {chosen_word}. You lose one life mann ")
        if lives==0:
            game_over = True
            print(f"You lose\n {stages[lives]} ")
        else:
            print(f"{stages[lives]}")


    if "_" not in display:
        game_over=True
        print("You Won")


