# Logical Operators

# We haven't checked for multiple conditions in same
# line of code
# if condition1 & condition2 & condition3:
#   do this
# else:
#   do this

# how to combine conditions ?
# To do this
# we need to learn

# Logical Operators
# A and B   - Both the conditions need to be True
# C or D    - Either of the two conditions need to be True
# not E     - Reverses the condition (flips the condition)


# Again for roller coaster problem.
# Free ticket for people in midlife crisis (45 - 55)

# Age 45 to 55 Modifier
# Update the code so that people age 45 to 55 (inclusive of both)
# rides for free. Use logical operators to check the age is greater
# than 45, and it's also less than 55

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

    # elif 45 <= age <= 55:   # It's not easier to understand
    elif age >= 45 and age <=55:    # There is a warning, it's telling that there's a simpler way of writing it.
        print("No ticket for midlife crisis")
    else:
        print("Adult Tickets are $12")
        bill = 12

    wants_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No -> ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3   # Augmented Assignment or Assignment Operator

    print("Your final bill is {}".format(bill))
else:
    print("Sorry! You have to grow taller before you can ride.")
