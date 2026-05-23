import random
import maths



def mutate(a_list):
    b_list = []
    new_item = 0

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# What we do first is we can define a breakpoint, the red highlight
# then we click on debug
# a breakpoint - puts a break on the code at that particular line
# it shows us all the windows in the typing window

# then we are going to use first of the step buttons in the debugger
# step over - it executes our code line by line, stopping at the very next line.
# the highlighted line is going to execute next.
# and the line above it is the line that has been executed.

# step into button
# it is going to execute the code line by line, but when it encounters a line
# such as line 12 above, where we are using another module, it's going to get
# into the definition of that function and shows us how that function works for us

# when we are done exploring it
# step out button - we can use it to get out of the code that we are examining in another module


# step into my code
# just like the step into, it executes the code line by line, it ignores the library functions,
# but it steps into the code that we created, like the maths module that we created
# and imported, like on line 13. We can step out of it as weell.
# useful when we have multifile project.


# We got Threads & variables tab below and console tab as well
# Threads and variables can be really helpful, showing us the values of the variables that we've
# got going on.
# Console
# This tab shows what gets printed in the run of the code.
