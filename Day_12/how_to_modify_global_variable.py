# How to modify the global variable

# A variable with global scope
enemies = 1

def increase_enemies():
    # enemies = 2
    # This is a variable with local scope, we are basically creating a completely new variable entirely separate from the one
    # in the global scope. It's not changing anything in the global variable

    global enemies
    # but what if we want to modify the variable in the global scope ?
    enemies += 1 # This has started to highlight with an error, editor thinks that we are trying to tap into a local variable
    # that we haven't declared.
    # we want to tap into global 'enemies' variable
    # for that, we have to use the 'global' keyword to tell that we have a global variable which is
    # called enemies that is defined somewhere outside the function and that's the variable we
    # want to modify inside the function.


    print(f"enemies inside function : {enemies}")

print(enemies)


# it's a terrible idea to call the local and global variable with the same name.


# we don't want to do it often, because it's very confusing.
# avoid modifying the variable inside the function


# how to achieve this without modifying the global variable
# use return for this.
