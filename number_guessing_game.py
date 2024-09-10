import random
import number_guessing_game_art

num = 0

def compare(guess):
    if guess == num:
        print(f"You got it! The answer was {num}.")
        return True
    elif guess < num:
        print("Too low.")
    elif guess > num:
        print("Too high.")
    return False

def play_game():
    global num
    attempts = 0
    print(number_guessing_game_art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty choice. Defaulting to 'easy'.")
        attempts = 10

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if compare(guess):
            break
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")


play_game()
