fruits = ["strawberries",  "Nectarines", "Apples", "Grapes",
          "Peaches", "Cherries", "Pears",]

vegetables = ["spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Some of them are fruits and some of them are vegetables
# Let's also separate fruits and vegetables but also keep them
# in dirty_dozen list
# We can use Nested List

dirty_dozen = [fruits, vegetables]
# Above means, we have inserted fruits list at 0 index and vegetables
# list in index 1

print(dirty_dozen)
# [
#   ['strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'],
#   ['spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
# ]
# The list looks like this.

print(dirty_dozen[1][1])
