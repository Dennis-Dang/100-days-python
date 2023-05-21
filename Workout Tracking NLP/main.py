import datetime as dt
import pytz
import requests
import time
from urllib.error import HTTPError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import dotenv_values

config = dotenv_values('.env')
BASE_API_URL = 'https://trackapi.nutritionix.com'


def update_sheet(body):
    try:
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!A2',
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
    except HTTPError as e:
        if e.code == 429:
            time.sleep(60)
            update_sheet(body)


query = input("Enter your query: ")
header = {
    "x-app-id": config["APP_ID"],
    "x-app-key": config["API_KEY"]
}
request_body = {
 "query": query,
 "gender": "male",
 "weight_kg": config["WEIGHT"],
 "height_cm": config["HEIGHT"],
 "age": config["AGE"]
}
now = dt.datetime.now()
tz = pytz.timezone("US/Pacific")
tz.localize(now)
date_time = now.strftime("%m/%d/%Y %I:%M:%S %p").split(' ')

response = requests.post(f"{BASE_API_URL}/v2/natural/exercise", headers=header, json=request_body)
exercise_data = response.json()['exercises'][0]
values = [[date_time[0], date_time[1]+' '+date_time[2], exercise_data['name'].title(), exercise_data['duration_min'], exercise_data['nf_calories']]]
# Create the OAuth 2.0 flow
flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
credentials = flow.run_local_server()

# Build the Google Sheets API service
service = build('sheets', 'v4', credentials=credentials)

spreadsheet_id = '1Fbfqds8bdsuNDUe2wgd77zpNL2w6vfZOaQq3h7L1FaA'
sheet_name = 'Sheet1'


append_body = {
    "values": values
}

update_sheet(append_body)
