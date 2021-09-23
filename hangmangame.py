import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_lenght = len(chosen_word)
lives = 6
display = []
print(hangman_art.logo)
for x in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:\n").lower()
    for x in display:
        if guess == x :
            print(f"{guess} opps these letter already present")

    for x in range(0, len(chosen_word)):
        if chosen_word[x] == guess:
            display[x] = chosen_word[x]
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("you win")
    if guess not in chosen_word:
        lives -= 1
        print(f"sorry '{guess}' this letter is not there in a word")
        print(hangman_art.stages[lives])
    if lives == 0:
        end_of_game = True
        print("Game over out of lives")