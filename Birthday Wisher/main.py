import smtplib
import datetime as dt
import pandas
import random
from dotenv import dotenv_values

config = dotenv_values(".env")
templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
username = config["DEV_EMAIL"]
password = config["EMAIL_PASSWORD"]

# Get today's date
today = dt.datetime.today().date()
# Read Birthdays.csv file
birthdays = pandas.read_csv("birthdays.csv")
# Gather all birthdays matching today's date (month and day)
filtered_birthdays = birthdays[(birthdays['day'] == today.day) & (birthdays['month'] == today.month)]
birthday_list = filtered_birthdays.to_dict(orient="records")
#   If there is any birthdays for today:
if len(birthday_list) != 0:
    # Choose a random template
    chosen_template = random.choice(templates)

    # For each person who has a birthday today:
    for person in birthday_list:
        with open(file=f"./letter_templates/{chosen_template}") as file:
            message = file.read()
            # Replace the greeting with the recipient's name
            message = message.replace('[NAME]', person['name'])
            print(message)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(from_addr=username,
                                to_addrs=person['email'],
                                msg=f"Subject: Happy Birthday!\n\n{message}")
