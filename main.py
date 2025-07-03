"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Michal Hurai
email: michal@hurai.sk
"""

import random


def generate_secret_number():
    """
    Generates a random 4-digit number as a string.
    The number does not start with zero and has unique digits.
    """
    digits = list('123456789')  # First digit cannot be zero
    first_digit = random.choice(digits)
    digits = list('0123456789')
    digits.remove(first_digit)
    random.shuffle(digits)
    return first_digit + ''.join(digits[:3])


def calculate_bulls_and_cows(secret, guess):
    """
    Compares the secret number and user's guess.
    Returns the number of bulls (correct digit in correct position)
    and cows (correct digit in wrong position).
    """
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows


def play_game():
    """
    Main function to play the Bulls and Cows game.
    Handles input, validation, and game loop.
    """
    secret = generate_secret_number()
    attempts = 0
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    while True:
        guess = input("Enter a number: ")
        if not guess.isdigit():
            print("Invalid input. Please enter digits only.")
            continue
        if len(guess) != 4:
            print("Invalid input. Please enter exactly 4 digits.")
            continue
        if guess[0] == '0':
            print("Invalid input. The number cannot start with zero.")
            continue
        if len(set(guess)) != 4:
            print("Invalid input. The digits must be unique.")
            continue
        attempts += 1
        bulls, cows = calculate_bulls_and_cows(secret, guess)
        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")
        print("-" * 47)
        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            print("-" * 47)
            print("That's amazing!")
            break


if __name__ == "__main__":
    play_game()
