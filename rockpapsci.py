import random as r
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image=[rock,paper,scissors]

while True:
    choice = int(input("Choose your choice 0:Rock. 1:Paper, 2:Scissors"))
    comchoice = r.randint(0, 2)
    print(f"computer:{image[comchoice]}\n")
    if choice < 0 or choice >= 3:
        print("Please enter the Valid input to play the game you lose\n")
    elif choice == 0 and comchoice == 2:
        print(f"user:{image[choice]}\n")
        print("You Won! You have good luck maybe\n")
    elif comchoice == 0 and choice == 2:
        print(f"user:{image[choice]}\n")
        print("You lost better luck next time\n")
    elif comchoice > choice:
        print(f"user:{image[choice]}\n")
        print("You lost better luck next time")
    elif comchoice < choice:
        print(f"user:{image[choice]}\n")
        print("You Won! You have good luck maybe\n")
    elif choice == comchoice:
        print(f"user:{image[choice]}\n")
        print("it is draw\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

