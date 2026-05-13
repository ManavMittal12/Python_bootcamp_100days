import random
from idlelib.debugobj import dispatch
from os.path import sep
from shlex import split

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    # if display == "":
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    '''else:
        for letter in chosen_word:
            if letter == guess:
                new_guess_index = chosen_word.index(guess)
                # display[new_guess_index] = letter   # This won't work because string are not mutable
    '''
    print(display)
    if "_" not in display:
        game_over = True
