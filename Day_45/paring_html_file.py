# We are going to parse an HTML file using beautiful-soup library
# parsing the HTML file is; the first step to extracting the data contained in a website.


# using the beautiful soup -
# is used to pull data from HTML and XML files.
# HTML and XML are both structural languages, and they are responsible for
# structuring data like the data in a website using these tags.


# importing beautiful soup
from bs4 import BeautifulSoup
# for lxml parsers
# import lxml


# we have to get hold of the website file in a string or as a piece of text.

with open("website.html") as website:
    web_data: str = website.read()

soup: BeautifulSoup = BeautifulSoup(web_data, "html.parser")    # the whole soup object represents our html code.

# we get the title tag. (beautiful soup makes the sense of the website using the html parser)
print(soup.title)

# title.name
print(soup.title.name)
print(soup.title.string)

# print(soup)
print(soup.prettify())

# gives the first anchor tag
print(soup.a)

# gives the first li
print(soup.li)



# what if we want all the paragraphs of the paragraphs?
