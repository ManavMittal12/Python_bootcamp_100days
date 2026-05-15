from art import logo


def highest_bidder(bid_dict):
    max_bid = float('-inf') # that's how you declare infinity
    highest_biddr = None
    for hbu in bidder_dict:
        if bidder_dict[hbu] > max_bid:
            max_bid = bidder_dict[hbu]
            highest_biddr = hbu

    print(f"Bid won ${max_bid} by {highest_biddr}")


print(logo)
# TODO-1: Ask the user for input
new_bidder = True

bidder_dict = {}
while new_bidder:
    user_name = input("Please enter your name : ")
    user_bid = int(input("Please enter your bid : $" ))
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

    bidder_dict[user_name] = user_bid


    another_bidder = input("Are there more bids ? 'Yes' or 'No' : ").casefold()
    if another_bidder == "no":
        new_bidder = False
    else:
        print("\n" * 100)

# TODO-4: Compare bids in dictionary
highest_bidder(bidder_dict)
