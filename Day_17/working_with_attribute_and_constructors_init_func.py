# How do we create attribute for a class

# class User:
#     pass


# user_1 = User()

# easiest ways is to simply tap into the object and add an attribute
# user_1.id = "001"
# user_1.username = "Batman"

# print(user_1.username)

'''
class User:
    pass


user_1 = User()


user_1.id = "001"
user_1.username = "Batman"

if we had lots of attributes and everytime we had a new user, and we had 
to do same thing, like this putting the attribute, that would be tough.

how can i make it easier for me ? 

'''


'''
Constructor
Which is part of the blueprint that allows us to specify what should happen when our object is being constructed.
also known as initializing an object 
When the object is initialized, we can set variables or counters to their starting value 


In python, to create a constructor 
is by using a special function
__init__

class Car:
    def __init__(self):
    # initializes attributes 

it has two __ underscores __ on both side of the name, this means that 
it's a method that the python interpreter knows about and knows that it has a 
special function.

what is the special function ? It is normally used to initialize the attributes.
'''


class User:
    # inside the class, we initialize init function
    def __init__(self, user_id, user_name):
        self.id = user_id       # self.id is the attribute that is going to be associated with this class and we can then
        # set it to user_id that is passed in
        self.user_name = user_name
        self.followers = 0

        # we can name either of these anything we want, the attribute and the parameter
        # there is a convention to have the name of the parameter same as the name of the attribute,
        # but we don't always have to follow.


        # inside the init function, is where we initialize or create the starting values for our attributes
        # One important thing to remember is the init function will be called everytime you create a new object from this class

        # for example, if we print
        print("new user being created .....")
        # everytime, we initialize a new user, this print statement is going to be created.


user_1 = User("001", "Batman")
user_2 = User("002", "Micheeeheeeal")


print(user_1.user_name, user_1.id)


'''
How do we set attributes in our constructor ? 

syntax 

class Car:
    def __init__(self, seats):
        self.seats = seats
        
inside the init function
self - is the actual object that's being created or being initialized.
we can add as many parameters as we want 
those parameters are going to be passed in when an object gets constructed 
from this class
Once you receive that data, you can use to set the object attributes.

if in our init function, there is a parameter, we can pass in some data to those 
parameters which will be used to set the attributes for that object.

my_car = Car(5)
my_car.seats will be equal to 5 

It makes it a lot quicker when making a lot of objects.


remember that, when you add parameters to the constructor, that is the init function,
you are now saying that whenever a new object is being contructed from this class, it must provide 
thesee two peices of data shown in example. Otherwise it will give error.


# Sometimes, we want to provide default values to start with and 
if at some later point in our program, we want to modify it,
then we can do it at that point. 

it doesn't make sense for the attribute to initialize only when we are loading up the attribute. 

in our outer example, like we have initialized 
self.followers = 0

and we are not going to pass it from our object creation 
'''

print(user_1.followers)
