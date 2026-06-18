# Learning to Write, Read and Update JSON data in password manager.
# meaning JavaScriptObjectNotation
# Originally designed for javascript but because it has simple structure
# and is easy to understand, it was adopted by python as well.

# it's kind of similar to dictionary
# composed with a bunch of nested lists and dictionaries.


'''
{
    "Amazon" : {
        "email" : "batman@email.com",
        "password" : "5fBraA$uSA5"
    },
    "Twitter" : {
        "email" : "batman@email.com",
        "password" : "!gVfPVihW&4pM"
    }
}
'''
import json

# That's the find of data we are aiming for
# to work with json data in python, we can use the inbuild json library

# Write
json.dump()
# Read
json.load()
# update
json.update()
