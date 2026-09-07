# Rendering HTML Elements in Python.

from flask import Flask

app = Flask(__name__)
# Flask accept HTML in the return.
# for example, if we want to create H1, we can do that

# if we want to give some inline CSS
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'

# what if you want to render more than one HTML element.
# all you had to do is continue typing, meaning add more tags.

@app.route("/page1")
def this_is_second_page():
    # since it's not recommended to write long lines of code in a single line because it's difficult to read
    # we can split the string and use a backslash and split the string in multiple line
    # which is equivalent a single line.
    return '<h2 style="text-align: center">This is page2</h2>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3cyMXh1dXZwYW9wOHBwcWN2Y3ZzNzN2bnQ0YmZkemQ0Z3hjbWlmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT9IgG50Fb7Mi0prBC/giphy.gif" width=600>'

# we can add other attributes to the image tag, like we can edit the width
# we can also add GIF on our img tag.
# As we change our source attributes, or the style attributes, the text
# that is going in there is going in as a string with the quotation mark.
# So, this will clash with outer quotation marks. Make sure to use quotes properly.


if __name__ == "__main__":
    app.run(debug=True)
