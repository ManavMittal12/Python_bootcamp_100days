# Docstrings

# are basically a way for us to create some documentation as we
# code our functions or a block of code.


# When we use the functions in built in python, we can see documentations
# we can write the same kind for our functions using the docstrings


# Docstrings has to go as the first line after the declaration. define the name of your function, the inputs and then after the colon, the first indented line
# will be the docstring. We have to use three quotation marks, and in between them, we write the documentation
# In this, we write what the function is going to do, or what our future self of another user should no about.
# With doc strings, we can write things multi line.
#  You can use triple quotes to write multi line comments as well.
# Official python guidance is to avoid multiline comments like these
def format_name(lname, fname):
    """Take a first and last name and format it to return the title case version of the name
    """
    formatted_f_name = fname.capitalize()
    formatted_l_name = lname.capitalize()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_name  = format_name("bAtman", "WAYNE")
