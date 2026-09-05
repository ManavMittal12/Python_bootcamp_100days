import special_attribute_in_python


# One of the common ways that we'll see flask apps is
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

# __main__ denotes the file that is currently being run.
