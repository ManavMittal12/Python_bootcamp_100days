# Coffee Machine Project

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


QUARTERS = 0.25 # $
DIMES = 0.10 # $
NICKLES = 0.05 # $
PENNIES = 0.01 # $


def dispense_coffee(user_choice):
    resources["water"] -= MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    if user_choice != "espresso":
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    else:
        resources["milk"] -= 0

    print(f"Here is your {user_choice}☕🍵. Enjoy!")


def display_report(money):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: {money}$")


def check_resources(user_choice):
    if resources["water"] >= MENU[user_choice]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[user_choice]["ingredients"]["coffee"]:
            if user_choice != "espresso":
                if resources["milk"] >= MENU[user_choice]["ingredients"]["milk"]:
                    return True
                else:
                    return "Sorry there is not enough milk"
            else:
                return True
        else:
            return "Sorry there is not enough coffee"
    else:
        return "Sorry there is not enough water"


def input_coins():
    print("Please insert coins.")
    user_quarters = int(input("how many quarter?: "))
    user_dimes = int(input("how many dimes?: "))
    user_nickles = int(input("how many nickel?: "))
    user_pennies = int(input("how many pennies?: "))
    total_amount_inserted = (user_quarters*QUARTERS) + (user_dimes*DIMES) + (user_nickles*NICKLES) + (user_pennies*PENNIES)

    return total_amount_inserted


def check_user_amt_to_cost(coin_amt_inserted, user_choice):
    global money_collected
    if coin_amt_inserted >= MENU[user_choice]["cost"]:
        if coin_amt_inserted > MENU[user_choice]["cost"]:
            refund_amt = coin_amt_inserted - MENU[user_choice]["cost"]
            money_collected += MENU[user_choice]["cost"]
            print(f"Here's your {round(refund_amt, 2)}$ change")
        else:
            money_collected += MENU[user_choice]["cost"]
        return True
    else:
        return "Sorry that's not enough money. Money refunded."


coffee_machine_working = True
money_collected = 0


while coffee_machine_working:
    user_coffee_choice = input("What would you like ? (espresso/latte/cappuccino): ").casefold().strip()


    if user_coffee_choice in ("espresso", "latte", "cappuccino"):
        sufficient_amount = check_user_amt_to_cost(input_coins(), user_coffee_choice)
        if sufficient_amount is True:
            resource_status = check_resources(user_coffee_choice)
            if resource_status is True:
                dispense_coffee(user_coffee_choice)
            else:
                print(resource_status)
        else:
            print(sufficient_amount)
    elif user_coffee_choice == "report":
        display_report(money_collected)
    elif user_coffee_choice == "off":
        coffee_machine_working = False
        print("The coffee machine is off!")
    else:
        print("Incorrect Option, Try Again")
