# __name__ and __main__ : Special Attributes built into python

print(__name__)
# the above code prints
# __main__

# python has some special attributes, that are built into python,
# at any point, we can tap  into the name to find out what is the current class,
# function, methods, or descriptor's name.

# we're executing the code in a particular module.

# when we write
if __name__ == "__main__":
    # execute only if run as a script
    print("Run when ran as  script ")

# it's run as a script or from interactive prompt, but is not run from an imported
# module.

print("run when ran as a imported module.")

# continued in test.py file
