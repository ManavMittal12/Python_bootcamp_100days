# Files

# File system and how we can open, read, write and close them again

# Reading and Writing

# to open file
file = open("my_file.txt")  # takes no of input
# file we wanna open, the mode and other things
# file name mentioned as a string
# And we store it into a variable.


# Now, we want to read the file,
# this read method returns the contents of the
# file as a string
contents = file.read()
print(contents)
# content from our file gets printed.


# After we are done with our file, at the end,
# we also have to close it.
file.close()

# why do we want to close?
# When python opens a file, it takes up some of the
# resources of the computer and at some point later on
# it might decide to close it and free up the resources,
# but we don't know when that might happen and if it will happen.

# So, instead, we tell it to close down the file manually with this code
# "file.close()"

# it's like opening tabs in the browser, it will take resources,
# when we close it, the resources are given back.



# It's kind of hard to remember to close the file when doing multiple things
# Instead, we can do a different method

# we can use "with keyword"
# then open function with the file name as string
# then as keyword and the variable we want to bound to it.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)



# what if instead of reading, we want to write to it.
# we can use, write() function to write to it.
# the "mode" parameter in open function is set to "r" by default
with open("my_file.txt", mode="w") as file:
    file.write("I am going to learn Agentic AI")    # it will give error,
    # if we don't mention our file to open in write mode.
    # After executing the above code, all the previous text is deleted
    # replaced by the text we mentioned.



# if we don't want to delete the contents of the file, but add to it,
# we can use the mode "a", append
with open("my_file.txt", mode="a") as file:
    file.write("\nI am also learning Python")
# append adds to the end of the last text.



# One of the important things to know is, when opening a file in "w" write mode
# and it does not exist, then, python is going to create a new file for us.
with open("new_file.txt", mode="w") as file_2:
    file_2.write("Lmao!")
