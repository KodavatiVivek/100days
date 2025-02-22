import random as r
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def cal_score(cards):
    score= sum(cards)
    if score==21 and len(cards)==2:
        return 0
    elif 11 in cards and score>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def deal_card():
    deal=r.choice(cards)
    return deal

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def black_jack():
    user_cards = []
    com_cards = []
    com_score = -1
    user_score = -1
    is_gameover = False
    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())
    while not is_gameover:
        user_score = cal_score(user_cards)
        com_score = cal_score(com_cards)
        print(f"Users cards are :{user_cards} userScore:{user_score}\n")
        print(f"computer cards are :{com_cards[0]}\n")
        if user_score == 0 or com_score == 0 or user_score > 21 or com_score > 21:
            is_gameover = True
        else:
            draw = input("Do you want draw a new card yes:y and no:n\n").lower()
            if draw == "y":
                user_cards.append(deal_card())
            else:
                is_gameover = True

    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = cal_score(com_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {com_cards}, final score: {com_score}")
    print(compare(user_score, com_score))

while input("Do you want play again Y: True N: False").lower() == "y":
    print("\n" * 20)
    black_jack()



