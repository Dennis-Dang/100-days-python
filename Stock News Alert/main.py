from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "GOOGL",
    "apikey": config["ALPHAV_API_KEY"]
}
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
daily_stock = [value for (key, value) in stock_data.items()]
yesterdays_closing = daily_stock[1]['4. close']
day_before_yesterdays_closing = daily_stock[2]['4. close']


closing_diff = abs(float(yesterdays_closing) - float(day_before_yesterdays_closing))
delta_percent = (closing_diff / float(yesterdays_closing)) * 100

if delta_percent > 2:
    print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use Telegram API
# Send a separate message with the percentage change and each article's title and description to your telegram account.


# Optional: Format the Telegram message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

