import requests
import requests_cache
from datetime import datetime, timedelta
import smtplib
import html


STOCK : str = "TSLA"
COMPANY_NAME : str = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock():
    with open("D:/Computer_Science_Learning_Material/api_keys/alphavantage_api.txt") as stock_api_file:
        stock_api = stock_api_file.read()

    with requests_cache.enabled('stock_cache.db'):
        parameters = {
            "function" : "TIME_SERIES_DAILY",
            "apikey" : stock_api,
            "symbol" : STOCK,
        }

        response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
        response.raise_for_status()
        stock_data = response.json()

    yesterday_stock_price = float(stock_data["Time Series (Daily)"][f"{datetime.today().date() - timedelta(days=1)}"]["4. close"])
    day_before_stock_price = float(stock_data["Time Series (Daily)"][f"{datetime.today().date() - timedelta(days=2)}"]["4. close"])
    difference = abs(yesterday_stock_price - day_before_stock_price)
    difference_percent = round((difference / yesterday_stock_price) * 100, 2)

    return difference_percent


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_company_news() -> tuple:
    """
    Get 3 news article pieces
    :param company_name:
    :return news_articles:
    """

    news_articles: list = []
    date_today = datetime.today().date()
    date_yesterday = date_today - timedelta(days=5)
    with open("D:/Computer_Science_Learning_Material/api_keys/get_news_api.txt") as news_api_file:
        news_api_key: str = news_api_file.read()

    with requests_cache.enabled('news_cache.db'):
        parameters = {
            "apiKey" : news_api_key,
            "q" : COMPANY_NAME,
            "from" : date_today,
            "to" : date_yesterday,
            "language" : "en",
        }

        response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
        response.raise_for_status()
        news_data = response.json()

    for i in range(3):
        news_articles.append([news_data["articles"][i]["title"], news_data["articles"][i]["description"]])

    return tuple(news_articles)



## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

# setting up smtp
percentage_diff = get_stock()
my_email = "iambatman@batcave.com"
with open("D:/python_google.txt") as pass_file:
    password = pass_file.read()
if percentage_diff > .100:
    for news in get_company_news():
        msg = f"Subject: {news[0]}\n\nOur stock: {STOCK} has percentage change of about {percentage_diff}% \n\nHere are some news articles -->\n{news[1]}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=msg.encode('utf-8'))


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
