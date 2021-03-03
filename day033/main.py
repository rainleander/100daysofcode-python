import requests
from datetime import datetime

MY_LAT = 53.173180
MY_LONG = 6.602950

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# response.raise_for_status()
#
# """
# 1xx: hold on
# 2xx: here you go
# 3xx: go away
# 4xx: you screwed up
# 5xx: i (the server) screwed up
# """
#
# data = response.json()
# # {'iss_position': {'longitude': '74.1416', 'latitude': '4.4747'}, 'message': 'success', 'timestamp': 1614750671}
# print(data)
# data = response.json()["iss_position"]
# # {'longitude': '74.1416', 'latitude': '4.4747'}
# print(data)
# data = response.json()["iss_position"]["latitude"]
# # 4.4747
# print(data)


#----- Sunrise Sunset Challenge -----#
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

"""
You can call the API via the browser with the JSON viewer installed in a better format
via: https://api.sunrise-sunset.org/json?lat=53.173180&lng=6.602950&formatted=0
"""

time_now = datetime.now()
print(time_now.hour)
