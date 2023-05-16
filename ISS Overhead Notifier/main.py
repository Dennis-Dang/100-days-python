from dotenv import dotenv_values
import requests
import smtplib
import datetime as dt

config = dotenv_values(".env")
# LATITUDE = float(config["LATITUDE"])
# LONGITUDE = float(config["LONGITUDE"])
# TODO Remove this later, these are debug values.
LATITUDE = 14.00
LONGITUDE = -25.00
EMAIL = config["DEV_EMAIL"]
PASSWORD = config["DEV_EMAIL_PASSWORD"]

USER_EMAIL = config["CLIENT_EMAIL"]

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"


def is_overhead(iss_lat, iss_lon):
    if abs(iss_lat - LATITUDE) <= 5 and abs(iss_lon - LONGITUDE) <= 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "formatted": 0
    }
    sunset_response = requests.get(SUNSET_SUNRISE_API_ENDPOINT, params=parameters)
    sunset_response.raise_for_status()
    # Sample response:
    # {
    #   'results':
    #       {'sunrise': '2023-05-16T05:31:44+00:00',
    #       'sunset': '2023-05-16T18:21:00+00:00',
    #       'solar_noon': '2023-05-16T11:56:22+00:00',
    #       'day_length': 46156,
    #       'civil_twilight_begin': '2023-05-16T05:10:08+00:00',
    #       'civil_twilight_end': '2023-05-16T18:42:36+00:00',
    #       'nautical_twilight_begin': '2023-05-16T04:43:22+00:00',
    #       'nautical_twilight_end': '2023-05-16T19:09:22+00:00',
    #       'astronomical_twilight_begin': '2023-05-16T04:16:10+00:00',
    #       'astronomical_twilight_end': '2023-05-16T19:36:34+00:00'},
    #   'status': 'OK'
    # }

    # Extract sunset and sunrise data
    sunset_data = sunset_response.json()['results']['sunset']
    sunrise_data = sunset_response.json()['results']['sunrise']
    # Extract hour from sunset and sunrise data
    sunset_hour = int(sunset_data.split('T')[1].split(':')[0])
    sunrise_hour = int(sunrise_data.split('T')[1].split(':')[0])

    # Get current hour
    now = dt.datetime.now()
    current_hour = int(now.strftime("%H"))

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    else:
        return False


response = requests.get(ISS_API_ENDPOINT)
response.raise_for_status()
# Sample response:
# {
#     'iss_position':
#         {
#             'latitude': '-14.4829',
#             'longitude': '143.1410'
#         },
#     'timestamp': 1684218732,
#     'message': 'success'
# }
ISS_data = response.json()
ISS_lat = float(ISS_data['iss_position']['latitude'])
ISS_lon = float(ISS_data['iss_position']['longitude'])
print(ISS_data)
# If ISS is approximately above (+/- 5 degrees) the user's coordinates:
if is_overhead(ISS_lat, ISS_lon):
    print("Is overhead")
    # Check if it's night. Use datetime module to check if it's past sunset.
    if is_night():
        print("It's night")
        # Send an email notification that the ISS is nearby above the sky.
else:
    print("Not Overhead")

