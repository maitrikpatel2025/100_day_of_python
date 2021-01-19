from art import logo,vs
import random
from game_data import data


def player(participant):
    return f" {data[participant]['name']}, {data[participant]['description']}, {data[participant]['country']} "

def compare(player_a, player_b):
    if data[player_a]['follower_count'] > data[player_b]['follower_count']:
      return player_a
    elif data[player_b]['follower_count'] > data[player_a]['follower_count']:
      return player_b

def selected_player(your_guess,a,b):
  if your_guess.lower() == "a":
    return a
  elif your_guess.lower() == 'b':
    return b

def random_player():
  return random.randint(0,49)

print(logo)
player1 = random_player()
score = 0
winner = player1

print(f"compare A: {player(player1)}")

end_game = False
while not end_game:
  print(vs)
  player2 = random_player()
  print(f"Against B: {player(random_player())}")
  guess = input("who has a more followers? Type 'A' or 'B' : ")
  if winner == selected_player(guess,player1,player2):
    winner = compare(player1, player2)
    score += 1
    print("_______________________")
    print(f"Your are right. current score {score}")
    print(f"compare A: {player(winner)}")
  elif winner != selected_player(guess,player1,player2):
    end_game = True
    print("_______________________")
    print(f"sorry that's wrong. Final_score: {score}")

