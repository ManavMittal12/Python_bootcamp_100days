# Adding Methods to a Class

# Attributes are the things that object has
# Methods are the things that the object does.


'''
For example in a Car Class, we have an attribute of seats,
and we create a methods to make the car adapt to the race mode

e.g.

class Car:

    def __init__(self):
        self.seats = 5
    A function attached to an object is a method.
    def enter_race_mode():
        self.seats = 2


car1 = Car()
to call a method, you need to get hold of the object ,and you use the dot notation
to call the methods

car1.enter_race_mode()
'''


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        # Default attributes.
        self.followers = 0
        self.following = 0

        print("new user being created .....")

    # we want to have a way for the users to follow each other, their follower counts go up

    def follow(self, user):
        # Unlike the functions, the methods always needs to have a self parameter as the first parameter.
        # this means that when these methods are called, it knows the object that calls in.
        user.followers += 1
        self.following += 1     # Self keyword becomes very important when we are working with classes and objects.
        # it's a way for us to refer to the object that is going to be created from this class inside the class blueprint.
        # you won't see self when you are using the objects, but you'll see them a lot when you're writing the
        # code inside your class.



user_1 = User("001", "Batman")
user_2 = User("002", "Micheeeheeeal")

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)

print(user_1.user_name, user_1.id)
