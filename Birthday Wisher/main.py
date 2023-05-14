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
# Read Birthdays.csv file
# Gather all birthdays matching today's date (month and day)
#   If there is any birthdays for today:
#       For each person who has a birthday today:
#           Select a random letter template
#           Replace the letter's greeting with the recipient's name
#           Send email to recipient
