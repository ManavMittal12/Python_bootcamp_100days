from art import logo


def add(n1, n2):
    """
    Add two values received as parameter
    """
    return n1 + n2


def sub(n1 , n2):
    """
    Subtract two values received as parameter
    """
    return n1 - n2

def multipy(n1, n2):
    """
    Multiply two values received as parameter
    """
    return n1 * n2

def divide(n1, n2):
    """
    Divide two values received as parameter
    """
    return n1 / n2


arithmetic_operations = {
    "+" : add,
    "-" : sub,
    "*" : multipy,
    "/" : divide,
}



print(logo)

def calculator():
    calculation_continue = True
    n1 = float(input("Please input your first number -> "))

    while calculation_continue:
        user_operation = input("+\n-\n*\n/\nPick one operator --> ").strip()
        n2 = float(input("Please input your second number ->"))
        result = arithmetic_operations[user_operation](n1, n2)
        print(f"{n1} / {n2} = {result}")

        want_to_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation or just type anything else to exit --> ").casefold()
        if want_to_continue in ("y", "yes"):
            n1 = result
        elif want_to_continue in ("n", "no"):
            calculation_continue = False
            print("\n" * 200)
            calculator()    # This will go back to the code and execute the function program again until the user chooses something else.
            # This is called recursion
        else:
            calculation_continue = False

calculator()
