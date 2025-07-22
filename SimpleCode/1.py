# Guess the Number Game

# 1. Importing random module
import random

# 2. The program picks a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 20.")

# 3. Let the user guess up to 5 times
for guess_count in range(1, 6):
    guess = int(input("Take a guess: "))  # 4. Get user input as integer

    # 5. Check if the guess is correct
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {guess_count} tries.")
        break  # Exit the loop if guessed correctly

# 6. If the number was not guessed in 5 tries
if guess != secret_number:
    print(f"Sorry! The number I was thinking of was {secret_number}.")
