import requests
from dotenv import dotenv_values
import re

config = dotenv_values('.env')


class FitTracker:
    def __init__(self):
        self.endpoint = "https://pixe.la"
        self.token = config["TOKEN"]
        self.username = config["USERNAME"]
        if self.token and self.username:
            self.header = {
                "X-USER-TOKEN": self.token
            }
        else:
            self.header = self.create_user()

    def create_user(self):
        token = input("Type in your token: ")
        while not re.match(r"^[\w\D]{8,128}$", token):
            print("Token must alphanumeric (a-z)(A-Z)(0-9)")
            token = input("Type in your token: ")
        username = input("Type in your username")
        while not re.match("^[a-z][a-z0-9]{1,32}$", username):
            print("Username must be within 32 characters in length, "
                  "start with a letter, followed by alphanumeric characters.")
            username = input("Type in your username: ")

        pixela_parameters = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users", json=pixela_parameters)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())
            return response.json()

    def create_graph(self):
        graph_format = {
            "id": "graph1",
            "name": "Exercise Tracker",
            "unit": "Reps",
            "type": "int",
            "color": "sora",
            "timezone": "America/Los_Angeles"
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users/{self.username}/graphs", json=graph_format,
                                     headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            graph_data = response.json()
            print(graph_data)

    def add_pixel(self, quantity: str, graph_id: str, date: str):
        pixel_parameters = {
            "date": date,
            "quantity": quantity
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users/{self.username}/graphs/{graph_id}",
                                     json=pixel_parameters,
                                     headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())

    def update_pixel(self, graph_id: str, date: str, quantity: str):
        pixel_parameters = {
            "quantity": quantity
        }
        try:
            response = requests.put(f"{self.endpoint}/v1/users/{self.username}/graphs/{graph_id}/{date}",
                                    json=pixel_parameters,
                                    headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())

    def delete_pixel(self, graph_id: str, date: str):
        try:
            response = requests.delete(f"{self.endpoint}/v1/users/{self.username}/graphs/{graph_id}/{date}",
                                   headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())
