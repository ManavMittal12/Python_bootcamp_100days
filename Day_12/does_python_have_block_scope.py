# Does python have block scope ?


# unlike other programming languages, there is not such thing as block scope in
# python

if 3 > 2:
    a_variable = 10     # if you put a variable inside a block of if, or while loop, basically
                        # any sort of block of code that is indented, that is not fenced.
                        # it will have the same scope as the enclosing function or if there is not enclosing function
                        # it has global scope.


# eg
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

new_enemy = ""
if game_level < 5:
    new_enemy = enemies[0]      # even tho this new_enemy variable is created within the if block. If i go outside the if block


print(new_enemy)    # this is perfectly valid code and will print the value
# we are getting this warning from the limited, that the local variable might we accessed before the assignment

# to get rid of it, you can declare the variable outside the loops or conditions and modify it
# like
# new_enemy = ""

'''

withing the function

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]     


print(new_enemy)  # this would error out, because within the function local scope comes into play. to print this, we have to be 
within the function boundary to print it.
'''
