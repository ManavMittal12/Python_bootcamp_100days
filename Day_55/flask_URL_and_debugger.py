# Working flask URL Paths and the Flask Debugger.


# first task is to get hold of what the user typed in the url
# or known as parsing the URL

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")  # This is a decorator function, that lives in the app object declared in Flask class.
def bye():
    return "Bye!"

# what if we want to have a variable in that route.
# getting hold of what user types in here.


# we have to use variable rules.
# we can add variable sections to URLs. by marking it with <variable name> syntax.
# our function will receive it once our decorator is done with it, and then we can
# use it in our function.


@app.route("/username/<name>")  # Flask will turn whatever comes after /username/<variable name>
def greet(name):
    return f"Hello {name}"


# for our changes to be reflected, we need to stop and refresh our server.
# if we are testing and developing our website, this is really painful
# to run and rerun our code.


# there's a debug mode and it has a few advantages.
# it allows us to activate the debugger which helps us narrow down on issues
# it activates the reloader,
# and it activates the debugger on flask application.

# we can add even more to the path
@app.route("/username/<name>/1")  # Flask will turn whatever comes after /username/<variable name>
def greet1(name):
    return f"Hello {name} lol!"





# we can do other things like debug an issue.
# when we do something wrong, we get flask debug view.


# what we can do is, we can open the flask debugger with the button on the right.
# it will ask for the pin that is there in our console.
# we need to provide this key to it.
# it opens up a console, and we can start diagnosing.



# there's also a converter, which can convert the URL into any datatype
# that we specify. by default, it converts url into a string
# meaning, it will accept any text without a slash
@app.route("/username/<path:name>")    # here, we are telling that the data type is going to be a path, and then we gonna save that as name
def greet2(name):
    return f"Hello {name} lol!"
# the whole path will be rendered.

# we can have more than one variable as well.
@app.route("/username/<name>/<int:number>")
def new_function(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True) # changing the debug property to true.
