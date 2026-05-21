# Namespace: Local vs Global Scope

# Scope
# Imagine, you have a house with a fence around it, and you plant an apple tree
# in your garden, Only you and your family can access it.
# What if you plant an apple tree in the neighborhood or on the sidewalk
# it would be free for all access to those apples.
# That's how you can understand scope


enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")   # This will print 2


increase_enemies()
print(f"enemies outside function: {enemies}")   # This will print 1


# Scope is very important in programming

# another example
# Local Scope
# exists within functions

# def drink_potion():
#     # maybe it would have a variable created inside a function
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)  # it will give error, name-error.It says the name is not defined
# even when we have defined it inside the function.

# It goes back to the local scope
# when you create a new variable or a new function in a function, it can be only used inside the function.
# what if we want it to be accessible outside the function,
# we have to think about global scope
# the difference between global and local scope is where you define your variable

# Global scope
player_health = 10  # It's accessible everywhere in the file. It has a global scope. It's at the top level of the file
# meaning it's not within a function

def drink_potion():
    potion_strength = 2 # Local Variable
    print(player_health)    # It will print here even when it's declared outside the function


drink_potion()


# This concept of local and global is applied not only to variable but also to functions and anything that
# you can name.
# This concept is known as 'Namespace'.
# Anything that you give the name to is namespace and is valid to scopes

def game():
    def drink_potion(): # Now this function is withing the game, and it local to it
        potion_strength = 2
    print(player_health)

    # we have to call the drink_potion() function from inside.
    drink_potion()

# drink_potion() This will give error because the function is inside game() function


# You have to be aware of the namespaces you are creating
