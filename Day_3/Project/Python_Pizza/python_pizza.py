# Python Pizza

print("Welcome to Python Pizza")
user_selection = input("What size pizza do you want? ->"
      "\n1)Small\n2)Medium\n3)Large\n>>> ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_bill = 0

if user_selection == "Large":
    final_bill += 25
    if pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
    print(f"Your pizza is {user_selection} and final bill is {final_bill}")

elif user_selection == "Medium":
    final_bill += 20
    if pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
    print(f"Your pizza is {user_selection} and final bill is {final_bill}")

elif user_selection == "Small":
    final_bill += 15
    if pepperoni == "Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1
    print(f"Your pizza is {user_selection} and final bill is {final_bill}")

# What if the user types something wrong ?
else:
    print("Wrong Input, Try again.")
