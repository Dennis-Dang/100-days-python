from dotenv import dotenv_values
import requests
from haversine import haversine, Unit
import datetime as dt
import smtplib

config = dotenv_values(".env")
# Client's Coordinate position
LATITUDE = float(config["LATITUDE"])
LONGITUDE = float(config["LONGITUDE"])

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUNSET_SUNRISE_API_ENDPOINT = "https://api.sunrise-sunset.org/json"

# Viewable distance at a 40 degree height above the horizon.
# This is approximated by taking the average altitude of the ISS, 253 miles.
# flyover_distance = 253 / tan(40) ~ 301.51366
flyover_distance = 301


def is_overhead(iss_lat, iss_lon):
    """Determines whether the ISS is within viewable range. Uses the haversine formula to calculate distances between
    two points on a sphere. However since the Earth is slightly ellipsoidal, the calculation is accurate enough.
    :param iss_lat ISS's latitude coordinate position
    :param iss_lon ISS's longitude coordinate position
    :returns True if the ISS is within viewable range, otherwise returns false."""
    if haversine((iss_lat, iss_lon), (LATITUDE, LONGITUDE), unit=Unit.MILES) <= flyover_distance:
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

# If ISS is approximately above (+/- 5 degrees) the user's coordinates:
if is_overhead(ISS_lat, ISS_lon):
    # Check if it's night. Use datetime module to check if it's past sunset.
    if is_night():
        message = "The ISS is flying is overhead, look outside and spot it!"
        # Send an email notification that the ISS is nearby above the sky.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=config["DEV_EMAIL"], password=config["DEV_EMAIL_PASSWORD"])
            connection.sendmail(from_addr=config["DEV_EMAIL"],
                                to_addrs=config["CLIENT_EMAIL"],
                                msg=f"Subject: ISS is nearby!\n\n{message}")
