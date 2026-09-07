## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticate_decorator(function):
    def wrapper(*args, **kwargs):
        # The condition is self-explanatory, the only problem is that
        # this user is undefined. we are able to pass function, but what if
        # we want to pass in arguments associated with that function.
        # for that, we can use args and kwargs.
        if args[0].is_logged_in:
            # now after, adding args and kwargs, it's going to look at the
            # function that is going to be passed in which is going to have
            # some inputs, and it's going to take the first positional input
            # , and then see if it is logged in property is equal to true.
            function(args[0])
    return wrapper


@is_authenticate_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

# In the above code, we want the users to create a blog post,
# that can be achieved only by the users who are logged in.
# we have to check and authenticate if they are logged in


new_user = User("Batman")
new_user.is_logged_in = True
create_blog_post(new_user)

# what if we want to create a decorator function which can decorate
# any function on our website that requires authentication.

# requires that the user is_logged_in property is set to true.
# creating a decorator above "is_authenticated_decorator"
