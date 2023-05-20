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


def add_pixel(quantity: str, graph_id: str, date: str):
    pixel_parameters = {
        "date": date,
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


commands = '''
Add: Add an entry to the tracker for a day.
Modify: Modify an entry.
Delete: Delete an entry.
Settings: Configure account settings.
'''

print("Welcome to the Habit Tracker, what would you like to do?")
print("What would you like to do? "+commands)
to_do = input("> ").lower()
while 'exit' != to_do:
    if to_do == 'add':
        print("Enter the date you want to add the entry for. (YYYY-MM-DD)\n"
              "Or press Enter to submit as today's date.")
        str_date = input("> ")
        str_date = str_date.strip()
        date = None
        if not str_date:
            date = dt.datetime.today()
        else:
            try:
                date = dt.datetime.strptime(str_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date. Date must be formatted YYYY-MM-DD")

        if date:
            try:
                print(f"How many sit-ups did you do on {date.strftime('%Y-%m-%d')}?")
                quantity = int(input("> "))
            except ValueError:
                print("Quantity must be a number. Try again.")
            else:
                print(f"You've done {quantity} sit-ups on {date}. Confirm? (Y/N)")
                confirm = input("> ").lower()
                if confirm == 'y':
                    try:
                        add_pixel(config['GRAPH_ID'], date.strftime("%Y%m%d"))
                    except Exception as e:
                        print("Uh oh, could not submit pixel: " + e)
                    else:
                        print("Pixel added successfully.")

    print("\nWhat would you like to do?"+commands)
    to_do = input("> ").lower()
