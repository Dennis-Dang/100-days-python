import requests
from urllib.error import HTTPError
from dotenv import dotenv_values
import re
import os
import time
import pyinputplus as pyip

config = dotenv_values('.env')


class FitTracker:
    def _update_env(self):
        with open('.env', 'w') as file:
            for key, value in self.ids.items():
                file.write(f'{key}={value}\n')
        os.environ.update(self.ids)

    def __init__(self):
        self.endpoint = "https://pixe.la"
        self.ids = {}
        try:
            self.ids = {
                "TOKEN": config["TOKEN"],
                "USERNAME": config["USERNAME"],
                "GRAPH_ID": config["GRAPH_ID"]
            }
        except KeyError as e:
            if e.args[0] == 'TOKEN' or e.args[0] == 'USERNAME':
                if 'yes' == pyip.inputYesNo("Account not found in '.env' file.\n "
                                            "Do you wish to create an account? (Y/N) "):
                    self.ids["TOKEN"] = ""
                    self.ids["USERNAME"] = ""
                    self.create_user()
                else:
                    quit()

            if e.args[0] == 'GRAPH_ID':
                if 'yes' == pyip.inputYesNo("Graph not found in '.env' file.\n "
                                            "Do you wish to create an account? (Y/N)"):
                    self.ids["GRAPH_ID"] = ""
                    self.create_graph()
                else:
                    quit()

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

    def delete_user(self):
        choice = pyip.inputMenu([self.ids['USERNAME'], "other username", "return"],
                                f"Do you want to delete {self.ids['USERNAME']}, or a different user?\n")
        username: str
        token: str
        if choice == "other username":
            username = input("Please specify which username you want deleted: ")
            token = input(f"Please enter {username}'s token: ")
        elif choice == self.ids["USERNAME"]:
            username = self.ids["USERNAME"]
            token = input(f"Enter the token for {username}: ")
            if token != self.ids["TOKEN"]:
                print("Incorrect token received. Returning to menu.")
                return
        else:
            return

        delete_header = {
            "X-USER-TOKEN": token
        }

        confirm = pyip.inputYesNo(f"You are about to delete {username}, this action is irreversible.\n"
                                  f"(Unless there's an error)\nConfirm? (Yes/No) ")
        if confirm == 'yes':
            try:
                response = requests.delete(f"{self.endpoint}/v1/users/{username}", headers=delete_header)
                response.raise_for_status()
            except Exception as e:
                print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
            else:
                print(response.json())
                if choice == self.ids['USERNAME']:
                    self.ids['USERNAME'] = ''
                    self._update_env()

    def create_graph(self):
        graph_id = input("What do you want the graph id to be? ")
        while not re.match("^[a-z][a-z0-9]{1,16}$", graph_id):
            print("Graph ID must be within 16 characters in length, "
                  "start with a letter, followed by alphanumeric characters.")
            graph_id = input("What do you want the graph id to be? ")
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

    def add_pixel(self, quantity: str, date: str):
        pixel_parameters = {
            "date": date,
            "quantity": quantity
        }
        try:
            response = requests.post(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/graphs/{self.ids['GRAPH_ID']}",
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

    def delete_pixel(self, date: str):
        try:
            response = requests.delete(f"{self.endpoint}/v1/users/{self.ids['USERNAME']}/"
                                       f"graphs/{self.ids['GRAPH_ID']}/{date}",
                                       headers=self.header)
            response.raise_for_status()
        except HTTPError as e:
            while e.code == 503:
                print("Pixela is temporarily unavailable, retrying request..")
                time.sleep(1)
                self.delete_pixel()
        except Exception as e:
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        else:
            print(response.json())
