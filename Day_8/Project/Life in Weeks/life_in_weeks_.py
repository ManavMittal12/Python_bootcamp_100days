# Life in weeks
import math

def life_in_weeks(age):
    days = 365
    weeks = math.floor(days / 7)
    weeks_in_90_years = 90 * weeks
    weeks_in_user_age = age * weeks
    total_weeks = weeks_in_90_years - weeks_in_user_age
    print(f"You have {total_weeks} weeks left.")


age = int(input("Please enter your current age -->"))
life_in_weeks(age)
