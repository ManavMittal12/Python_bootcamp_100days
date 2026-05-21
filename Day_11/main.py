from art import logo
import random
def deal_card():
    """
    Returns a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if c_score == 0:
        return "You Lose, Computer has a black jack"
    elif u_score == 0:
        return "You win"
    elif u_score == c_score:
        return "Draw"
    elif u_score > 21:
        return "You lost, It's a bust"
    elif c_score > 21:
        return "You win, Computer got a bust"
    else:
        if u_score > c_score:
            return "You win"
        else:
            return "You lose"


def blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1 # Since we can't set it no 0
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_new_card = input("Do you want to draw a new card ? 'Y' or 'N' -->").strip().casefold()
            if draw_new_card in ("y", "yes"):
                user_cards.append(deal_card())
            elif draw_new_card in ("n", "no"):
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n")
    print(compare(user_score, computer_score))
    print("\n")
    print(f"User's final hand : {user_cards}, User's final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, Computer's final score {computer_score}")



while input("Do you want to play a game of Blackjack? 'Y' or 'No' -->>").casefold() == "y":
    print("\n" * 1000)
    blackjack()
