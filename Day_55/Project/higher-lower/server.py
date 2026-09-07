# Higher Lower Project with Flask

from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)

@app.route("/")
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bDl1ZmxnajgyMDdtOGk1OWtwY3o0aXc2aXJ6MGl0ZW9lcm1kbzhtMiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/39V7Yg3swPRv2/200.webp">'


@app.route("/<int:user_num>")
def user_guess(user_num):
    if 0 <= user_num <= 9:
        if user_num < random_number:
            return f"<h1 style='color:red'>Too Low, try again!</h1>" \
                    "<img src='https://i.giphy.com/jD4DwBtqPXRXa.webp'>"
        elif user_num > random_number:
            return f"<h1 style='color:purple'>Too High, try again!</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        else:
            return f"<h1 style='color:green'>You found me!</h1>" \
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    else:
        return '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXRoZ2hoNzBuZzFoY3VxbXU0aTIyaGVhYzhucjJ0cGJhYXAxanZoYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/449dnLNnyYgNas2e03/giphy.gif" width=200><br>' \
               '<b>You guessed out of scope, Try Again!</b>'


if __name__ == "__main__":
    app.run(debug=True)
