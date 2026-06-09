# List Comprehension
# Unique to the Python language. Not many programming languages have
# access to it or anything close to it.


# e.g.
# for loop
num = [1, 2, 3]
new_list = []
for n in num:
    add_1 = n + 1
    new_list.append(add_1)



# using list comprehension
# keywords method - where we type out the list comprehension keywords, and replace
# each of the item with actual item in your code.

# e.g.
# new_list = [new_item for item in list]
# name of the new list, and instead of creating an empty list, we create straight into the
# same line
# then new item into the new_item and for loop.
            # expression "n+1"
new_list1 = [n+1 for n in num]
print(new_list1)


# we can also work with strings as well
# name = "Angela"
# new_list = [letter for letter in name]


name = "Angela"
new_list = [letter for letter in name]
print(new_list)


# python sequences
# list
# range
# string
# tuple
# they are called sequences, because they have an order
# when we perform list comprehension, it takes these sequence, and it's going
# to go through it in order be it the letters in the string, or the items in a
# list,
# and then it's going to take each of those items in the correct order and do
# something on it.


# Conditional List comprehension
# new_list = [new_item for item in list if test]
# we can tag on two more keywords, if and test
# the other code will run only when the test passes

# eg
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
shorter_names = [name for name in names if len(name) <= 4]
print(shorter_names)

long_name = [name.upper() for name in names if len(name) > 4]
print(long_name)
