from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
STOCK = "GOOGL"
COMPANY_NAME = "Tesla Inc"

# Use https://www.alphavantage.co
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": config["ALPHAV_API_KEY"]
}
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
daily_stock = [value for (key, value) in stock_data.items()]
yesterdays_closing = daily_stock[1]['4. close']
day_before_yesterdays_closing = daily_stock[2]['4. close']


closing_diff = float(yesterdays_closing) - float(day_before_yesterdays_closing)
up_down = ""
if closing_diff < 0:
    up_down = "🔻"
else:
    up_down = "🔺"
delta_percent = (abs(closing_diff) / float(yesterdays_closing)) * 100

if delta_percent > 2:
    # Use https://newsapi.org
    news_parameters = {
        "apiKey": config["NEWS_API_KEY"],
        "language": "en",
        "q": "Google",
        "searchIn": "title",
        "pageSize": "3"
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']

    messages = []
    for idx in range(len(news_data)):
        message = {
            "headline": news_data[idx]['title'],
            "brief": news_data[idx]['description']
        }
        messages.append(message)

    # Use Telegram API
    TOKEN = config["TELEGRAM_API_KEY"]
    CHAT_ID = config["TELEGRAM_CHAT_ID"]

    for message in messages:
        your_message = f"{STOCK}: {up_down}{round(delta_percent, 2)}%\n" \
                       f"Headline: {message['headline']}\n" \
                       f"Brief: {message['brief']}"
        SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': your_message})


# The format the of Telegram message looks like this:
"""
TSLA: 🔺2%
Headline: Google officially reveals the Pixel Fold. 
Brief: After months of rumors and leaks, Google has confirmed the Pixel Fold's existence. It showed off the foldable in
 an official capacity for the first time in a video posted on Twitter and YouTube. The company was expected to reveal 
 the Pixel Fold at Google I/O..
"""
