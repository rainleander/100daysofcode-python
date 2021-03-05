import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
