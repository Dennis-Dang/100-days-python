import datetime as dt
import pyinputplus as pyip
import requests

str_date = pyip.inputDatetime("What year do you want to travel to? Type in the date in this format YYYY-MM-DD: ",
                              formats=('%Y-%m-%d',))
date = str_date.date()

while date > dt.datetime.today().date():
    print(f"This is a date in the future, songs are not created yet for this date!\n"
          f"Enter a date before or on {dt.datetime.today().strftime('%Y-%m-%d')}.")
    str_date = pyip.inputDatetime("What year do you want to travel to? Type in the date in this format YYYY-MM-DD: ",
                                  formats=('%Y-%m-%d',))
    date = str_date.date()

# hot_100 = requests.get(f"https://www.billboard.com/charts/hot-100/{str_date}")
