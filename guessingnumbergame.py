# Number Guessing Game

secret = 7

print("Guess the number between 1 and 10")

# Keep asking until correct
while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
