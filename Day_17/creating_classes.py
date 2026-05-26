# How to create our own class in Python

# Class is a blueprint to create an eventual object.

'''
class Car:
the syntax is clear, we start with class keyword and then the name of the
class (*Keep the name of the class in Pascal case*)
'''


# We are creating a class for Users for a website
# it will tell what our user's have and what they can do.
# Everything that is going to go in the class will be indented with
# a semicolon.

'''
even though, we have nothing in our class, we can still initialize it 


class User:
    

object = Class    
user1 = User()  
'''

'''
pass keyword - If we want to leave a class or a function or anything that has a semicolon 
and expects an indentation, we can use the keyword pass.
All it does is passes. Works as a placeholder. 
'''

'''
-- naming the class, have the first letter of every word capitalized and this particular style of 
naming is called as PascalCase.
e.g. name of a person then, their first name and last name is capitalized 

-- camelCase - in camel casing, first word is lower case and every subsequent word is capitalized like 
pascal case

-- snake_case - every word is lower case and seperated by an underscore.

In python, camelCasing is not used much, PascalCase for class name and snake_case for almost everything else.
'''

class User:
    pass

user1 = User()
