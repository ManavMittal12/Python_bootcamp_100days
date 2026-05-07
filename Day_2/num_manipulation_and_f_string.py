# Number Manipulation and F String in Python

# In BMI calculator, we got a very long floating value.
# This is not ideal to output some number to the user
# we want it to be rounded

# How do we do that ?
# we can either convert it to integer and try printing it
# what this does is it floors the number, meaning, it removes the
# decimal values. Flooring it to lowest whole number

# but we don't want that. We want to perform the round function
# Where, when it's .5, it rounds up to next whole number and if it's
# below that, it rounds up to the lower whole number


bmi = 84/1.65**2
print(bmi)
print(int(bmi))
print(round(bmi))   # Really handy to work with function
# round takes two input
print(round(bmi,2)) # Second is number of digits you wanna round it to
# rounds to float number with two decimal places


# Assignment Operators
# such as addition assignment operator "+="
# will add the number on the right to the original value of the
# variable on the left and assign the new value to the variable.

# We have various
# +=
# -=
# *=
# /=

# Helps accumulate the results of our calculations
# eg

score = 0

# User scores a point
score += 1
print(score)


# F-strings
# In python, we can use f-strings to insert a variable
# or an expression into a string

# This is inconvenient
print("your score is" + str(score))

# Using f-string
score = 0
height = 1.8
is_winning = True

# Instead of using type conversions and plus signs
# we can use f string

# we put an f before the string double quotes
print(f"Your score is = {score}, your height is {height}. You are winning {is_winning}")  # this is an f string
