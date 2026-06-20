# Python Type Hints and Arrows

# we have seen data types in python.
# and we saw dynamic typing


# making code error-prone.
# age: int    # we can declare a variable and declare its data type
# and leave it as it is,  later on we got age from the user
# at that point we can set it
# age = 12
# and it's data type has to match it with the type annotated.


# we can do this with all basic data type
# age: int
# name: str
# height: float
# is_human: bool


# we can also declare type annotation in a function
# we can also declare a datatype for the return value of a function using (->)
# this feature if called type hint
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive



# if we wanna use this function with 100s of lines of code,
# we might forget what type of input it needs
# we can use declare type for the input to help ourselves.
if police_check(19):
    print("You may pass")
else:
    print("Pay a fine.")
