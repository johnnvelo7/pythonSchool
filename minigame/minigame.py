import random

def play_game ():
    # Generate a random number between 1 and 1000
    number = random.randint(1, 1000)
    print(number)
    max_guesses = 5
    num_guesses = 0

    while num_guesses < max_guesses:

        guess = int(input("Guess the number (between 1 and 1000): "))

        num_guesses += 1

        if guess == number:
            print(f"Congrats! You guessed the correct number in {num_guesses} attempt(s).")
            print(f"The number was: {number}")
            return True
        else:
            if guess > number:
                print(f"The {number} is too high.")
            else:
                print(f"The {number} is too low.")

        print(f"You have {max_guesses - num_guesses} guesses left.")

    print(f"Sorry!!! You fucked up.")
    print(f"The number was: {number}")
    return False

play_game()

while True:
    play_again = input("Do you want to play again? (YES/NO): ")
    if play_again.upper() == "YES":
        play_game()
    else:
        print("Thanks for playing bruh!")
        break


