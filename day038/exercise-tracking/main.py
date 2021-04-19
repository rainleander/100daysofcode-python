import requests
from datetime import datetime

APP_ID = "031d8a77"
API_KEY = "e526412b17bfa722fc3ad487a8b5d0f5"
TOKEN = "Bearer TheQuickBrownFoxJumpsOverTheå6514761241317;alksdjfhyqerpigunvz.kjxbcvil;uaehrwgt"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/a72fb3c79b3dabb89545d0ff6200f208/workoutTracking/workouts"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": TOKEN,
}

query = input("Tell me which exercises you did: ")

exercise_data = {
    "query": query,
    "gender": "female",
    "weight_kg": 80,
    "height_cm": 171,
    "age": 44,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_data, headers=exercise_headers)
result = exercise_response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

print(sheety_response.text)
