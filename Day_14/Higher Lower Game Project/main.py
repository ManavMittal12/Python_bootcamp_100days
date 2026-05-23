from art import logo, vs
from game_data import data
import random


def generate_option():
    """
    Generate a random choice from data and return it
    """
    random_generated_choice = random.choice(data)
    return random_generated_choice


def check_higher_follower(opt_a, opt_b):
    """
    Take the two options as input and compare them and return them
    """
    if opt_a["follower_count"] > opt_b["follower_count"]:
        return "a"
    else:
        return "b"



def check_user_input(hi_follow_count):
    """
    Take the option with higher follower count as input and check users selection against it. Return True or False
    """
    global user_score
    get_user_input = input("Who has more followers? Type 'A' or 'B': ").strip().casefold()

    if hi_follow_count == get_user_input:
        user_score += 1
        return True
    else:
        return False

print(logo)
option_A = generate_option()
user_score = 0
game_running = True

while game_running:

    option_B = generate_option()
    while option_A == option_B:
        option_B = generate_option()


    print(f"Compare A: {option_A["name"]}, a {option_A["description"]}, from {option_A["country"]}")
    print(vs)
    print(f"Against B: {option_B["name"]}, a {option_B["description"]}, from {option_B["country"]}")

    game_running = check_user_input(check_higher_follower(option_A, option_B))
    option_A = option_B
    if game_running:
        print("\n"*1000)
        print(logo)
        print(f"You're right! Current Score: {user_score}")
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {user_score}")
