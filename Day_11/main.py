from art import logo
import random


def deal_cards(list_of_cards):
    """
    Randomly appends the user's and computer's lists of cards using
    the random module.

    :param list_of_cards:
    :return None:
    """
    user_cards.append(random.choice(list_of_cards))
    computer_cards.append(random.choice(list_of_cards))


def calculate_score(u_cards, c_cards):
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    ace = 11

    u_cards.sort()
    c_cards.sort()
    if c_cards == [10, ace]:
        return user_sum, 0
    elif u_cards == [10, ace]:

        # if user_sum > 21:
        #     if ace in u_cards:
        #         pass

        return 0, computer_sum
    else:
        return user_sum, computer_sum

# Main Content
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

for _ in range(2):
    deal_cards(cards)

print(user_cards)
print(computer_cards)
users_score, computer_score = calculate_score(user_cards, computer_cards)
if computer_score == 0:
    print("Computer has Blackjack. Computer WON. User Lost")
elif users_score == 0:
    print("User has Blackjack. User WON. Computer Lost")
else:
    print(f"User score is : {users_score}\nComputer score is : {computer_score}")
