import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while True:  # Keep the game running until the correct guess
    guess = input("Enter your guess: ")

    if guess.isdigit():  # Check if input is a valid digit
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
            print(f"Enter a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"You've guessed it correctly! The answer was {answer}.")
            print(f"You guessed it in {guesses} tries.")
            break
    else:
        print("Invalid input.")
        print(f"Please enter a number between {lowest_num} and {highest_num}.")
