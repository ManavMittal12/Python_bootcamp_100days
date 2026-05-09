# Banker Roulette
import random


friends = ['Alice', 'Bob', 'Charles', 'David', 'Emanuel']

# 1)
random_choice = random.choice(friends)
print(f'The selected Debit card is from {random_choice}')


# 2)
rand_index = random.randint(0, 4)
print(friends[rand_index])
