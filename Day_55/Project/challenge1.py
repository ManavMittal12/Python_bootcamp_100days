from flask import Flask

app = Flask(__name__)

# Using more decorator calls to a function.
def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper



# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type.
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, You are {number} years old!"



if __name__ == "__main__":
    # Run the app in the debug mode to auto-reload
    app.run(debug=True)
