import requests
from dotenv import dotenv_values
config = dotenv_values('.env')

parameters = {
    "lat": config["LATITUDE"],
    "lon": config["LONGITUDE"],
    "units": "imperial",
    "exclude": "current,minutely,daily,alerts",
    "appid": config["OWM_API_KEY"]
}
response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
data = response.json()
# Get the first 12 hours of weather data.
hourly_weather = data["hourly"][:12]

# Sample Weather Hour Response:
# (The code above will filter weather data to have 12 of these)
# {
#     'dt': 1684317600,
#     'temp': 62.19,
#     'feels_like': 61.39,
#     'pressure': 1013,
#     'humidity': 70,
#     'dew_point': 52.3,
#     'uvi': 0,
#     'clouds': 0,
#     'visibility': 10000,
#     'wind_speed': 3.58,
#     'wind_deg': 166,
#     'wind_gust': 4.52,
#     'weather': [
#       {
#         'id': 800,
#         'main': 'Clear',
#         'description': 'clear sky',
#         'icon': '01n'
#       }
#     ],
#     'pop': 0
# }
rain = False
for hour in hourly_weather:
    for weather_condition in hour["weather"]:
        # Codes below 700 justify bringing an umbrella.
        # https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
        if weather_condition["id"] < 700:
            rain = True

if rain:
    # Send a Telegram message.
    your_message = "Bring an umbrella. 🌧☂"
    TOKEN = config["TELEGRAM_API_KEY"]
    CHAT_ID = config["TELEGRAM_CHAT_ID"]
    SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': your_message})
