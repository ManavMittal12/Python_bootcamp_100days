# print(len(12345))

# Consider functions a fancy machine in the factory
# That takes potato and converts the into chips
# it maybe does things internally, like cutting and frying

# What happens when we pass that machine a rock ?
# then we will get an error

# that's what happens here

# the len function doesn't like to work with the int
# that's why it gives us the type error

# In intellij/pycharm, we also get error message.

# to fix the type error above
print(len("1234"))


# In python, each function expects to work with a certain type of
# data type

# how do we know what data type does a data have ?
# we have a function called type()

print(type("Hello"))
print(type(123))
print(type(123.456))
print(type(True))
# Checking the data is called type checking


# What if we are not happy with the data type
# and want to change the data type
# it's called type casting in python (type conversion)

# eg
print(int("123 "))
print(int("123") + int("123"))
# dangerous things about it is, we can't convert something to
# another data type
# eg

# print(int("abc"))       # It will give value error, when we pass invalid
                        # literal

# can convert between
# int()
# float()
# str()
# bool()

# Challenge
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
