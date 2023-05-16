from dotenv import dotenv_values
import requests
import smtplib
import datetime

config = dotenv_values(".env")
LATITUDE = config["LATITUDE"]
LONGITUDE = config["LONGITUDE"]
EMAIL = config["DEV_EMAIL"]
PASSWORD = config["DEV_EMAIL_PASSWORD"]

USER_EMAIL = config["CLIENT_EMAIL"]

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"

# If ISS is approximately above (+/- 5 degrees) the user's coordinates:

# Check if it's night. Use datetime module to check if it's past sunset.

# Send an email notification that the ISS is nearby above the sky.
