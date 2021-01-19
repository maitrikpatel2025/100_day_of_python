#Step 1
import random
from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
display = []
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


for _ in range(word_length) :
    display.append("_")

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length) :
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
            print("====================================")
    print(f"{' '.join(display)}")
    print("====================================")

    if "_" not in display:
        end_of_game = True
        print("You win")
        print("====================================")
    print(stages[lives])