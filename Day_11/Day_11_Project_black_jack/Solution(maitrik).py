from art import logo
import random
import sys
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_card = []
computer_card = []
your_score = 0
computer_score = 0




def select_card(playing_for):
    if playing_for == "player":
        return random_select(your_card, 2)
    if playing_for == "computer":
        return random_select(computer_card,1)
    if playing_for == "another":
        return random_select(your_card,1)

def random_select(player,times):
    for card in range(0,times):
        player.append(random.choice(cards))
    return player

def calculate_score(card_list,score):
    for item in card_list:
        score += item
    return score

def check_winner(your_sco, com_sco):
    if com_sco > your_sco < 21:
        if com_sco > your_sco :
            return "You lose"
        elif your_sco > com_sco:
            return "you are winner"
    else:
        return "you lose"

blackjack = input("DO you want to play blackjack 'Y' or 'N' : ")
print(logo)
if blackjack.lower() == "y":
    select_card("player")
    select_card("computer")
    End_game = False
    while not End_game:
        print("")
        print(f"your cards : {your_card} current score : {calculate_score(your_card,your_score)}")
        print(f"computer first cards : {computer_card} current score : {calculate_score(computer_card,computer_score)}")
        print("")
        another_cards = input(" type 'y' to get another cards 'n' pass ")
        if another_cards == "y":
            select_card("another")
        elif another_cards == "n":
            select_card("computer")
            print("")
            print(f"your cards : {your_card} final score : {calculate_score(your_card,your_score)} ")
            print(f"computer first cards : {computer_card} final score : {calculate_score(computer_card,computer_score)}")
            print("")
            print(check_winner(your_score,computer_score))
            End_game = True
        else:
            another_cards = input(" type 'y' to get another cards 'n' pass ")

else:
    sys.exit(0)