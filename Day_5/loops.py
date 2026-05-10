# Loops
# To get things to be done over and over again

# 1st type of loop we see is - For Loop

# For Loop

'''
for item in list_of_items:
    # Do something for each item
'''

# it can be used really easily in combo with list

# eg

fruits = ["Apple", "Peach", "Pear"]
# If we want to access each item in this list individually
# and print it out one by one, then we would use for loops

# We start out with keyword "for" and then we give a name
# to a single item, so in this case, we call fruit
# then in keyword, and finally, the list that we want
# to loop through, which is our fruits here. and a colon
# next line is indented
"""for fruit in fruits:
   print(fruit)"""

# the loop is taking an item and assigning the fruit variable
# name to it, and then moves to next one and does the same.

# The loop allows us to execute the same line of code multiple times
# like here, print is getting executed multiple times.

# but our for loops is not limited to execute single statements
# we can execute a block of code multiple times.

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
print(fruits)

# Inside a for loop vs outside a for loop.
# Whenever you see a colon, in our if statement previously
# or the for loop that we're using here, the indentation is really
# important because if it's indented, means it's inside for loop

# for example, here we are printing fruits list outside the for loop,
# it's going to print it once.

# Indentation is really important.
