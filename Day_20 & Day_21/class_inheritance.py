# Class Inheritance

# For example, we code up a robot chef and give it bunch of functionality
# like bake(), stir() and measure() and then at some point, we decide that
# we also need a pastry chef. This pastry chef will need to know something that the
# chef knows how to do, but it also needs something extra, so we don't want to create
# this pastry chef entirely from scratch, instead what we wanna do is take the
# methods for the chef class and add to it.  like additional things like knead() and whisk()

# So this process of inheriting behavior and appearance from an existing class
# is known as class Inheritance.

# We can inherit both appearance and behavior, meaning attributes and methods.

# How does inheritance actually work in terms of code.

# for example, we created a class called fish, and it has an initialized.
'''
In order to get this Fish class to inherit from another class,
we have to add a set of parenthesis after the name of the class and
provide the class we want to inherit from.


class Fish(Animal):
    def __init__(self):
        super().__init__()  # To get hold of everything that an animal has and is so,
        # it's attributes and methods, all we have to do is, inside the init,
        # add "super().__init__()" and this super refers to this superclass,
        # So, basically initialize everything that the superclass can do in our
        # fish class.
'''

class Animal:
    def __init__(self):
        self.num_eyes = 2


    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self): # Inherits all the things from super class (Animal in this case).
        super().__init__()


    def swim(self):
        print("moving in water.")

# What if we want to modify a method from super class, or the class
# we are inheriting from.
# like breathe() in this case.

    def breathe(self):
        super().breathe()   # This will tell python, that we want to do everything that the
        # super class breathe() method does

        # and then we tell it to do something extra.
        print("Doing this underwater.")





nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
