import requests
from dotenv import dotenv_values
import datetime as dt
config = dotenv_values('.env')

parameters = {
    "lat": config["LATITUDE"],
    "lon": config["LONGITUDE"],
    "units": "imperial",
    "exclude": "current,minutely,daily,alerts",
    "appid": config["API_KEY"]
}
response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
print(response)
data = response.json()
print(data)

