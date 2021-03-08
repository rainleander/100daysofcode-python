import requests

## ----- Challenge: locate the hourly forecast for the next 48 hours ----- ##

parameters = {
    "lat": 53.173180,
    "lon": 6.602950,
    "exclude": "current,minutely,daily,alerts",
    "appid": "19e7f36aef01e2d3728ed9d2e0e3f630",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(f"The response for this call is {response.raise_for_status()}")

data = response.json()
print(data)
