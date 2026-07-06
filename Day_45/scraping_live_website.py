from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_data = response.text



soup: BeautifulSoup = BeautifulSoup(yc_web_data, "html.parser")

article = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in article:
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]



print(article_texts)
print(article_links)
print(article_upvotes)

highest_upvote_article = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote_article])
