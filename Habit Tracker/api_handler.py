import requests
from dotenv import dotenv_values

config = dotenv_values('.env')


class FitTracker:
    def __init__(self):
        self.endpoint = config["PIXELA_ENDPOINT"]
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
        username = input("Type in your username: ")
        pixela_parameters = {
            "token": token,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = requests.post(f"{self.endpoint}/v1/users", json=pixela_parameters)
        response.raise_for_status()
        print(response.json())

    def create_graph(self, name: str):
        graph_format = {
            "id": "graph1",
            "name": "Exercise Tracker",
            "unit": "Reps",
            "type": "int",
            "color": "sora",
            "timezone": "America/Los_Angeles"
        }
        response = requests.post(f"{self.endpoint}/v1/users/{config['USERNAME']}/graphs", json=graph_format,
                                 headers=self.header)
        response.raise_for_status()
        graph_data = response.json()
        print(graph_data)

    def add_pixel(self, quantity: str, graph_id: str, date: str):
        pixel_parameters = {
            "date": date,
            "quantity": quantity
        }

        response = requests.post(f"{self.endpoint}/v1/users/{config['USERNAME']}/graphs/{graph_id}",
                                 json=pixel_parameters,
                                 headers=self.header)
        response.raise_for_status()
        print(response.json())

    def update_pixel(self, graph_id: str, date: str, quantity: str):
        pixel_parameters = {
            "quantity": quantity
        }

        response = requests.put(f"{self.endpoint}/v1/users/{config['USERNAME']}/graphs/{graph_id}/{date}",
                                json=pixel_parameters,
                                headers=self.header)
        response.raise_for_status()
        print(response.json())

    def delete_pixel(self, graph_id: str, date: str):
        response = requests.delete(f"{self.endpoint}/v1/users/{config['USERNAME']}/graphs/{graph_id}/{date}",
                                   headers=self.header)
        response.raise_for_status()
        print(response.json())
