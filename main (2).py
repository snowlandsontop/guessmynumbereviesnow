import random
minimum = 1
maximum = 6
secret_number = random.randint(minimum, maximum)
def get_guess():
    guess = int(input(f"Guess a number between {minimum} and {maximum}: "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number!")
    else:
        print(f"You lose, the correct number was {secret_number}. Try again next time")
get_guess()  # call the function to start the game
