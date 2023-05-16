from dotenv import dotenv_values
import requests
import smtplib
import datetime

config = dotenv_values(".env")
# LATITUDE = float(config["LATITUDE"])
# LONGITUDE = float(config["LONGITUDE"])
# TODO Remove this later, these are debug values.
LATITUDE = 45.00
LONGITUDE = -65.00
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


response = requests.get(ISS_API_ENDPOINT)
response.raise_for_status()
ISS_data = response.json()
ISS_lat = ISS_data['iss_position']['latitude']
ISS_lon = ISS_data['iss_position']['longitude']
print(ISS_data)
# If ISS is approximately above (+/- 5 degrees) the user's coordinates:
if is_overhead(float(ISS_lat), float(ISS_lon)):
    print("Is overhead")
    # Check if it's night. Use datetime module to check if it's past sunset.
    # Send an email notification that the ISS is nearby above the sky.
else:
    print("Not Overhead")

