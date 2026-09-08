# Rendering HTML Files with Flask

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# How to render HTML files.
# Creating a server files as above
# figure out how to render HTML webpage, which is crafter in html file rather
# than string

# According to the flask documentation, flask looks for the
# html file in a folder called "Templates".
# we also have to import a method called "render_templates" from the
# flask package.
