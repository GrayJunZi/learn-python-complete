# 侩子手项目
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print(f"Solution {chosen_word}")

end_of_game = False
lives = 6

display = []
for i in range(len(chosen_word)):
    display += '_'

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
