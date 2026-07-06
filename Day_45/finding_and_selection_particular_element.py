# what if we want all the paragraphs of the paragraphs?
from bs4 import BeautifulSoup


with open("website.html") as website:
    web_data: str = website.read()

soup: BeautifulSoup = BeautifulSoup(web_data, "html.parser")


# till not we are getting hold of only the first tags
# what if we want all the tags.

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


all_para_tag = soup.find_all(name="p")
print(all_para_tag)


# what if we want only the text in the anchor tag ?
for tag in all_anchor_tags:
    print(tag.getText())
# above gets us the text


for tag in all_anchor_tags:
    print(tag.get("href"))  # will get us the links


# isolating an h1 by id.
all_tags = soup.find_all(name="h1", id="name")
print(all_tags) # gives us that particular element.


# we can do that with class attribute
print(soup.find(name="h3", class_="heading"))    # we get an error here, because class keyword is a reserved keyword in python # hence the class keyword is renamed to "class_"
print(soup.find(name="h3", class_="heading").getText())



# There are certain cases this might not work,
# what if we want a specific anchor tag, we have to find all anchor tag and then the specific. and it the website is complicated
# it would be difficult to figure out the one that we really want.

# we can use the css selectors using beautiful soup
# select_one method - select one will give us the first matching item
# select method - will give us all the matching items in the list

company_url = soup.select_one(selector="p a")   # we're looking for an "a" tag which sits inside p tag and this
# string is a css selector.
print(company_url)
# we can also select a class or id as well
company_url = soup.select_one(selector="#name")
print(company_url)
company_url = soup.select_one(".heading")
print(company_url)
