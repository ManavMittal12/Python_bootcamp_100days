"""
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:
"""

# BMI Calculator

# The body mass index (BMI) is a measure used in medicine to
# see if someone is underweight or overweight. This is the
# formula used to calculate it.

# bmi is equal to the person's weight divided by the person's height
# squared.

height = float(input("Please enter your height"))
weight = float(input("Please enter your weight"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
