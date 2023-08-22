import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while True:
        player_guess = int(input("Enter your guess: "))
        attempts += 1

        if player_guess < secret_number:
            print("Too low! Try again.")
        elif player_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
