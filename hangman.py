import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)  # Removed the real word print statement

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}.")
    else:
        guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, and that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word.upper()}! YOU LOSE")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    stages = hangman_art.stages
    print(stages[lives])
