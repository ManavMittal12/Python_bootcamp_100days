from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    choice = input(f"What would you like? ({menu.get_items()}) :").casefold().strip()


    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_in_menu = menu.find_drink(choice)
        if coffee_in_menu is not None:
            sufficient_resources = coffee_maker.is_resource_sufficient(coffee_in_menu)
            if sufficient_resources is True:
                get_money_machine = money_machine.make_payment(coffee_in_menu.cost)
                if get_money_machine is True:
                    coffee_maker.make_coffee(coffee_in_menu)
