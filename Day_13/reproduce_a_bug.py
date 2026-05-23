# Reproducing the bug that we encounter

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)        # After reproducing the bug by manually typing out indexes in the code,
# we came to know that 6 is producing the error because it's not in the list
dice_num = randint(1, 5)
print(dice_images[dice_num])


# Some bugs are sneaky, they only occur under certain conditions.
# In order to debug them, we need to be able to reliably reproduce
# the bug and diagnose our problem to figure out which conditions trigger the bug.
