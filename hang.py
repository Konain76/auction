import random

from hangman_words import word_list
from hangman_art import stages
chosen_word = random.choice(word_list)
lives=6
print(chosen_word)
display=[]
for y in chosen_word:
    display += ["_"]
print(display)
end_of_game=False
while not end_of_game:

    guess = input("guess a letter:\n").lower()
    if guess in display:
        print(f" you had already guessed:{guess}")

    for x in range(0, len(chosen_word)):
        letter = chosen_word[x]
        if letter == guess:
            display[x] = guess

    if guess not in chosen_word:
        print(f"{letter} this is not in the chosen_word")
        lives-=1
        print(stages[lives])
    if lives==0:
        end_of_game=True
        print("you lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("you win!")




