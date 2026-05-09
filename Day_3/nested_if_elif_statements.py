# Nested if statements and elif statements
# what if for the rollercoaster, we need to check another
# condition other than height ?

# if height > 120cms
# if for example, <=18 $7
# if >18 $12

# normal if else conditions have two statements
# if else
# we can write the code using only if-else condition as follows

# Nested if and else-if
height = int(input("Please enter your height in cms : "))
# age = int(input("Please enter your age : "))

# if height > 120:
#     if age <= 18:
#         print("You can ride the roller coaster for $7")
#     else:
#         print("You can ride the roller coaster for $12")
# else:
#     print("You have to grow taller to ride the roller coaster")

# Computer first looks for the outer block and then goes into the
# inner block of code.

# What if the conditions are more complex.
# eg
# <12 - "5$"
# 12-18 - "7$"
# >18  - "12$"
# There are three conditions

# To represent this, we can use elif
# if condition 1:
#     do A
# elif condition 2:
#     do B
# else:
#     do C

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age: "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You have to grow taller to go on the rollercoaster.")
