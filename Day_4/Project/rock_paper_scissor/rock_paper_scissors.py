import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_num_input = int(input("What do you choose ? Type 0 for Rock, Type 1 for Paper, Type 2 for scissors. -->"))
choices_available = ["rock", "paper", "scissors"]

if user_num_input == 0:
    user_choice = choices_available[0]
elif user_num_input == 1:
    user_choice = choices_available[1]
elif user_num_input == 2:
    user_choice = choices_available[2]
else:
    print("Invalid choice! Try Again!")
    user_choice = "No choice made"


computer_choice = random.choice(choices_available)
print(user_choice)
print(computer_choice)

if computer_choice == "rock":
    print(rock)
    print("Computer Chose: ")

    if user_choice == "rock":
        print(rock)
        print("It's a Tie")
    elif user_choice == "paper":
        print(paper)
        print("You Win")
    elif user_choice == "scissors":
        print(scissors)
        print("You lose")
    else:
        print("User Made no choice")

elif computer_choice == "paper":
    print(paper)
    print("Computer Chose: ")
    if user_choice == "rock":
        print(rock)
        print("You lose")
    elif user_choice == "paper":
        print(paper)
        print("It's a tie")
    elif user_choice == "scissors":
        print(scissors)
        print("You Win")
    else:
        print("User Made no choice")

elif computer_choice == "scissors":
    print(scissors)
    print("Computer Chose: ")
    if user_choice == "rock":
        print(rock)
        print("You Win")
    elif user_choice == "paper":
        print(paper)
        print("You lose")
    elif user_choice == "scissors":
        print(scissors)
        print("It's a tie.")
    else:
        print("User Made no choice")
