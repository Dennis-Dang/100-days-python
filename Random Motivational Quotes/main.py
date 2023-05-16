from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://zenquotes.io/api/random")
    data = response.json()[0]
    print(data["q"], data["a"])


