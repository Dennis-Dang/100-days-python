import requests
from dotenv import dotenv_values
import datetime as dt

config = dotenv_values('.env')
PIXELA_ENDPOINT = "https://pixe.la"

header = {
    "X-USER-TOKEN": config["TOKEN"]
}


def create_user():
    pixela_parameters = {
        "token": config["TOKEN"],
        "username": config["USERNAME"],
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(f"{PIXELA_ENDPOINT}/v1/users", json=pixela_parameters)
    response.raise_for_status()
    print(response.json())


def create_graph(name: str, ):
    graph_format = {
        "id": "graph1",
        "name": "Exercise Tracker",
        "unit": "Reps",
        "type": "int",
        "color": "sora",
        "timezone": "America/Los_Angeles"
    }
    response = requests.post(f"{PIXELA_ENDPOINT}/v1/users/{config['USERNAME']}/graphs", json=graph_format, headers=header)
    response.raise_for_status()
    graph_data = response.json()
    print(graph_data)


def add_pixel(quantity: str, graph_id: str):
    today = dt.datetime(year=2023, month=5, day=18)
    print(today.strftime("%Y%m%d"))

    pixel_parameters = {
        "date": "20230518",
        "quantity": quantity
    }

    response = requests.post(f"{PIXELA_ENDPOINT}/v1/users/{config['USERNAME']}/graphs/{graph_id}",
                             json=pixel_parameters,
                             headers=header)
    response.raise_for_status()
    print(response.json())


def update_pixel(graph_id: str, date: str, quantity: str):
    pixel_parameters = {
        "quantity": quantity
    }

    response = requests.put(f"{PIXELA_ENDPOINT}/v1/users/{config['USERNAME']}/graphs/{graph_id}/{date}",
                            json=pixel_parameters,
                            headers=header)
    response.raise_for_status()
    print(response.json())


def delete_pixel(graph_id: str, date: str):
    response = requests.delete(f"{PIXELA_ENDPOINT}/v1/users/{config['USERNAME']}/graphs/{graph_id}/{date}",
                               headers=header)
    response.raise_for_status()
    print(response.json())


update_pixel("graph1", "20230518", "40")
# delete_pixel("graph1", "20230518")
