from art import logo
import random


def set_difficulty():
    """
    Sets the difficulty for the game
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").casefold()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    return None


def computer_chooses_number():
    """
    Chooses a random number for computer and returns it
    """
    return random.randint(1, 100)

def guessing_game():
    """
    makes the user play the guessing game
    """
    is_game_over = False

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    no_of_attempts = set_difficulty()
    computer_choice = computer_chooses_number()


    while not is_game_over:
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == computer_choice:
            print(f"You got it! The answer was {computer_choice}.")
            is_game_over = True
        elif user_guess > computer_choice:
            print("Too High")
            print("Guess Again")
            no_of_attempts -= 1
        else:
            print("Too Low")
            print("Guess Again")
            no_of_attempts -= 1

        if no_of_attempts == 0:
            is_game_over = True
            print("You've run out of guesses. Refresh the page to run again.")




start_game = True

while start_game:
    if input("Do you want to play the Guessing game ?: 'Y' or 'N' --> ").casefold() in ("yes","y"):
        print("\n"*1000)
        guessing_game()
    else:
        start_game = False
