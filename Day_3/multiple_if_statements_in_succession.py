# Multiple if statements

# if / elif / else
# if condition1:
    # do A
# elif condition2:
    # do B
# else:
    # do C

# above we are checking only one condition, even when there's multiple
# because if one condition is true, python will bypass all the other
# once.

# What if we want to check multiple conditions even when other once are
# true

# Roller coaster
# Charge $3 dollars if user want to click a photo

# To do this
# we are going to write multiple if conditions -
# if condition 1:
#   do A
# if condition 2:
#   do B
# if condition 3:
#   do C


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >=120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5")
        bill = 5
    elif age <= 18:
        print("Youth Tickets are $7")
        bill = 7
    else:
        print("Ädult Tickets are $12")
        bill = 12

    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No -> ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3   # Augmented Assignment or Assignment Operator

    print("Your final bill is {}".format(bill))
else:
    print("Sorry! You have to grow taller before you can ride.")
