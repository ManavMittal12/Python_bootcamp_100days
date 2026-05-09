# Python Lists
# List is a data structure
# Data structure is a way of organizing and storing data

# ways of storing single pieces of data using single variables
# but we wanna store grouped pieces of data

# In some cases, we want to have order in our data. Like in Queue

## Lists help with that
# a set of square brackets
# with items in them,
# they can be any data type and
# multiple data types can be stored together
# Items are separated by a ','

# fruit = [item1, item2]

# Storing a bunch of fruits
fruits = ["Cherry", "Apple", "Pear"]


# for example, we wanna store the state of US
# They joined the Union in an Order
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia",
    "Connecticut", "Massachusetts", "Maryland", "South Carolina",
    "New Hampshire", "Virginia", "New York", "North Carolina",
    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
    "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
    "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
    ]

# Related data in order can be stored
# first data is first piece of data
# the order is not lost in the variable.
# and can be used in the same order
# we can use indexing to access that piece of data

print(states_of_america[0])


#######
              # 0       1        2
# fruits = ["Cherry", "Apple", "Pear"]
#######

# Instead of thinking of index about position, you think of it as an
# off set from the start of the list, then  in that case cherry is right
# at the beginning of the list so it has offset 0
# apple is shifter from the beginning by 1 and pear by 2
# this makes more sense.

# When you want to get hold of a particular piece of data stored inside
# a list, what you do is you get the name of the list and then
# you add a set of square brackets
# when you try to get items of the list, you use square brackets
# for indexing
# Inside the square brackets, you can provide the index of the item we
# want

# Instead of positive index, we can also use negative index.
# -1 , -2, and it starts from the end of the index
print(states_of_america[2])
print(states_of_america[-1])
# so far we have been pulling things out of list

# but we can also make change items in the list
# eg

states_of_america[1] = "Pencilvania"
# We changed Pennsylvania to Pencilvania
print(states_of_america)
# we can alter any item in the list using the above syntax

# If we want to add item to the list
# it will be added at the end.
states_of_america.append("Batcave Land")
# append adds single item to the end of the list
print(states_of_america)


# extend() - Extend the list by appending all the items from the iterable
states_of_america.extend(["AngelaLand", "Leave her johnny"])
print(states_of_america)
# https://docs.python.org/3/tutorial/datastructures.html -- for list
# Read through the data structures docs in documentation
