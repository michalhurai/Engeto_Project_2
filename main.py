"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Michal Hurai
email: michal@hurai.sk
"""

import random
def generate_secret_number():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])
def calculate_bulls_and_cows(secret, guess):
    bulls = sum([1 for s, g in zip(secret, guess) if s == g])
    cows = sum([1 for g in guess if g in secret]) - bulls
    return bulls, cows
def play_game():
    secret = generate_secret_number()
    attempts = 0
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    while True:
        print("Enter a number:")
        print("-" * 47)
        guess = input()
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with unique digits.")
            continue
        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")
        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            print("-" * 47)
            print("That's amazing!")
            break
if __name__ == "__main__":
    play_game()
