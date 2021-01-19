from art import logo
import random

attempts = 0
def game(guess):
    global attempts
    attempts -= 1
    if number_gussed == guess:
        return f"You gussed correct"
    elif number_gussed > guess:
        return f"Too Low \ntry again"
    elif guess > number_gussed:
        return f"Too high \ntry again"


print(logo)
print("""Welcome to the Number Guessing Game!
I'm think of a number between 1 and 100
""")
choice = input("Choose a difficulty. Type 'easy' or 'hard':")
if choice == 'easy':
    attempts = 10
if choice == 'hard':
    attempts = 5

number_gussed = int(random.randint(1, 100))

end_game = False
while not end_game:
    print("-------------------------")
    print(f"You have {attempts} left")
    guess_number = int(input("make a guess :"))
    print(game(guess_number))
    if guess_number == number_gussed:
        end_game = True
    if attempts == 0:
        end_game = True
        print("you are out of attempts")
        break
print("-------------------------")


