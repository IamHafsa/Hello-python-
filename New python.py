

# A simple number guessing game

import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

print("Guess the number I'm thinking of! It's between 1 and 10.")

# Allow the user to guess
user_guess = int(input("Enter your guess: "))

# Check if the guess is correct
if user_guess == number_to_guess:
    print("Congratulations! You guessed it!")
else:
    print(f"Sorry, the correct number was {number_to_guess}. Better luck next time!")



