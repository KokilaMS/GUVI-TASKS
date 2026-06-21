## Guess the Number Game##
import random
# 1. Computer randomly selects a number between 1 and 10
secret_number = random.randint(1, 10)
print("Welcome to Guess the number Game")
print("I am thinking of a number between 1 and 10.")

# Start with an incorrect guess to trigger the loop
guess = 0

# Loop until the player guesses the secret number
while True:
        # Get the player's guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
                print("Too High! Try again.")
        elif guess < secret_number:
                print("Too Low! Try again.")
        else:
                print("Correct! The secret number was",secret_number)
                break
print("Thank you for playing")

import random

# The list of words
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Pick a random word from the list
original_word = random.choice(words)

# 1. STRING MANIPULATION: Break the word into single letters
letters = list(original_word)

# Mix up the letters randomly
random.shuffle(letters)

# Stitch the mixed letters back into a single scrambled word
jumbled_word = "".join(letters)

# Print the game greeting and the puzzle word
print("WELCOME TO THE WORD SCRAMBLE GAME")
print("Unscramble this word:", jumbled_word)

# 2. LOOP: Keep asking for a guess over and over
while True:
        guess = input("Enter your guess: ")

        # 3. CONDITION: Check if the guess is right or wrong
        if guess == original_word:
                print("Correct! You unscrambled the word:",original_word)
                break  # This stops the loop immediately because the game is over
        else:
                print("Wrong answer! Try again.")
print("Thank you for playing")
