import requests
from datetime import datetime

APP_ID = "031d8a77"
API_KEY = "e526412b17bfa722fc3ad487a8b5d0f5"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = ""
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("Tell me which exercises you did: ")

exercise_data = {
    "query": query,
    "gender": "female",
    "weight_kg": 80,
    "height_cm": 171,
    "age": 44,
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
print(response.text)

today = datetime.now()
date = today.strftime("%d/%m/%Y")
