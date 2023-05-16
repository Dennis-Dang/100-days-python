import requests

# Generate 10 questions, of Category 'Science: Computers', question type True/False
parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
