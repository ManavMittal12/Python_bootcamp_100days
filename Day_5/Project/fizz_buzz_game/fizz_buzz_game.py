# Fizz Buzz Game

for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 != 0:
        print("Fizz")
    elif nums % 5 == 0 and nums % 3 != 0:
        print("Buzz")
    elif nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    else:
        print(nums)
