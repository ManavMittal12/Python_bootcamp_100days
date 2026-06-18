# Catching Exceptions : The try catch except finally pattern


# This will give us error
# with open("a_file.txt") as file:
#     file.read()

# FileNotFound
'''
try:
    file = open("a_file.txt")
except:     # we are getting a warning "too broad except clause."
    # according to the pep8 recommendations, we shouldn't use a bare except clause.
    # and mention the error we might get.
    file = open("a_file.txt", "w")
    file.write("Something")
# it's like we have if statement
'''

try:
    file = open("a_file.txt") # this will give us FileNotFound Error
    a_dictionary = {
        "key" : "value"
    }
    print(a_dictionary["key"])        # this will give us error, KeyError error but since it is
    # in try except block, we may never know about it
    # and we haven't even mentioned it also.

# we want our exception to  catch particular situation like
except  FileNotFoundError:  # it will execute except for filenotfound only and we will get key error
# except:     # we are getting a warning "too broad except clause."
    # according to the pep8 recommendations, we shouldn't use a bare except clause.
    # and mention the error we might get.
    file = open("a_file.txt", "w")
    file.write("Something")
# it's like we have if statement

# we can have multiple except statements
# except KeyError:
#     print("Key doesn't exist")
# in addition to simply catching the exception using except, we can
# get hold of the error message that would have normally printed had we
# not printed exception we called .
# normally. we get keyerror and get the message which kry is the problem.
# to get hold of the error message .
except KeyError as error_message:
    print(f"the Key {error_message} doesn't exist")
else:
    # it works when try succeeds.
    content = file.read()
    print(content)
finally:
    # runs no matter what happens
    file.close()
    print("File was closed")
    # not often used, but can be used for a code which we want to run no matter what.

# because this file doesn't exist.
# this is fair enough.

# We can get error often in our programs.
# the program doesn't get carried out once we get an error.

# So, we need to think about errors.

# KeyError
a_dictionary = {
    "key":"value"
}

# we will get an error because we are trying to access a key that
# doesn't exist in the dictionary we are trying to access
value = a_dictionary["non_existent_key"]


# IndexError
fruit_list = ["Apple", "Banana"]
fruit = fruit_list[3]   # we get an error because the index does not
# exist


# TypeError
# when we're trying to do something with particular piece of data,
# but we can't do that thing with a particular data type.
text = "abc"
print(text + 5)

# we have to plan for these eventualities.

# in programming, we can catch these exceptions.
# here's what the code looks like when we are dealing with the
# exceptions

# ----------------------------------------------
# try - something that might cause an exception
# except - Do this if there was an exception
# else - Do this if there were no exceptions
# finally - do this no matter what happens. (Used to clean things up)
# ----------------------------------------------
