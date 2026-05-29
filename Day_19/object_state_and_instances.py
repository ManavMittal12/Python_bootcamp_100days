# Object state and instances

# what if we need more turtle ?
# we need a class/ blueprint of what a turtle should behave like
# then we can create a turtle object from it.

# timmy : Turtle object = Turtle() : class from which we are creating
# we can create as many as we need.
# tommy = another turtle
# both turtle are separate from each other

# In programming, this is called separate instance,
# that means, each is the example of turtle objects.

# that means, at any moment in time, they can have different attributes
# and doing different things.
# in programming, it's called their state.

# for example, timmy has green color
# and tommy has purple color,
# meaning, they have different state.


import turtle

timmy = turtle.Turtle()
tommy = turtle.Turtle()


timmy.color("red")
tommy.color("black")
