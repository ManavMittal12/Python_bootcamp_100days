# Fixing errors and watching for red underlines
try:
    age = int(input("How old are you ?"))
except ValueError:
# After try, we add the except keyword, and then we add in the exception that we want to catch.
# And we tell if what happens is we end up with this error
    print("You have typed in an invalid number. Please try again with a numerical response such as '50'")
    # then we copy the code that takes the input
    age = int(input("How old are you ?"))


if age > 18:
    print(f"You can drive at age {age}")     # These types of bugs don't get highlighted, but we have to start on our toes. (like f is missing to initialize f-string)
# Now there's an underline, which shows us that there's an error waiting for us
# should work as a clue.


# if we give input as `twelve`, it will givee us error
# you can google errors to know that is going on


# How can we fix our code ?
# We can tell the user to give numbers

# or

# more robustly, we can use the
# Try, Catch block to catch exception in Python code

# So we know that the potential error is a value error, so we can catch
# our code and provide an alternative pathway for our code to go down.


# So we take the line  of the potentially dangerous code
# which is where we convert a string into an integer in this case
# we trap it inside a try block
