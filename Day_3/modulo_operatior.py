# Modulo Operator
# Looks like a percentage sign
# goes between two numbers, it's a binary operator
# and return the remainder of a division.

# Eg, 10 % 5 == 0

print(10%3)
# Remainer is 1, all the modulo does is returns the remainder

## Coding Challenge
# Write some code to check if the number in input area is
# odd or even. If it's odd, print out the work "odd" otherwise printout
# "even"

user_number = int(input("Please enter your number :"))

if user_number % 2 != 0:
    print("Odd")
else:
    print("Even")
