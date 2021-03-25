import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": $SECRET,
}


stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])

difference = abs(yesterday_closing_price - day_before_closing_price)
percent_diff = (difference / yesterday_closing_price) * 100

if percent_diff > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": $SECRET,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]

    three_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in news_data]
    print(three_articles[0])
    print(three_articles[1])
    print(three_articles[2])

    TWILIO_ACCOUNT_SID = $SECRET
    TWILIO_AUTH_TOKEN = $SECRET
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in three_articles:
        message = client.messages.create(
            body=article,
            from_=$SECRET,
            to=$SECRET
        )
