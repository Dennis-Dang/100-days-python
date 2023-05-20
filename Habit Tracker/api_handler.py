import requests
from dotenv import dotenv_values
import re
import os

config = dotenv_values('.env')


class FitTracker:
    def _update_env(self):
        with open('.env', 'w') as file:
            for key, value in self.ids.items():
                file.write(f'{key}={value}\n')
        os.environ.update(self.ids)

    def __init__(self):
        self.endpoint = "https://pixe.la"
        self.ids = {
            "TOKEN": config["TOKEN"],
            "USERNAME": config["USERNAME"],
            "GRAPH_ID": config["GRAPH_ID"]
        }
        if self.ids["TOKEN"] and self.ids["USERNAME"]:
            self.header = {
                "X-USER-TOKEN": self.ids["TOKEN"]
            }
        else:
            print("Username/Token not found.\n Creating one..")
            self.header = {
                "X-USER-TOKEN": self.create_user()
            }

        if not self.ids["GRAPH_ID"]:
            print("Graph ID not found.\n Creating one..")
            self.create_graph()

    def create_user(self):
        token = input("Type in your token: ")
        while not re.match(r"^[\w\D]{8,128}$", token):
            print("Token must alphanumeric (a-z)(A-Z)(0-9)")
            token = input("Type in your token: ")
        username = input("Type in your username: ")
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
            self.ids["TOKEN"] = token
            self.ids["USERNAME"] = username
            self._update_env()
            return token

    def create_graph(self):
        graph_id = input("What do you want the graph name to be?")
        graph_format = {
            "id": graph_id,
            "name": "Exercise Tracker",
            "unit": "sit-ups",
            "type": "int",
            "color": "sora",
            "timezone": "America/Los_Angeles"
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/graphs", json=graph_format,
                                     headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            graph_data = response.json()
            print(graph_data)
            self.ids["GRAPH_ID"] = graph_id
            self._update_env()

    def add_pixel(self, quantity: str, graph_id: str, date: str):
        pixel_parameters = {
            "date": date,
            "quantity": quantity
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/graphs/{graph_id}",
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
            response = requests.put(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/graphs/{graph_id}/{date}",
                                    json=pixel_parameters,
                                    headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())

    def delete_pixel(self, graph_id: str, date: str):
        try:
            response = requests.delete(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/graphs/{graph_id}/{date}",
                                       headers=self.header)
            response.raise_for_status()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())
