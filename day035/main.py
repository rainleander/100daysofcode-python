import requests
from twilio.rest import Client

parameters = {
    "lat": 53.173180,
    "lon": 6.602950,
    "exclude": "current,minutely,daily,alerts",
    "appid": "19e7f36aef01e2d3728ed9d2e0e3f630",
}

account_sid = "ACafc484d50575b604f88a750b1b1323e5"
auth_token = "771aa7dbd1f2946e2f6e1ba09fe6eea3"
client = Client(account_sid, auth_token)

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"]


def send_rain_alert():
    message = client.messages.create(
        body=" It's going to rain today. Bring an umbrella.️",
        from_='+12512501815',
        to='+31618547893'
    )

    print(message.status)


for x in range(12):
    if weather_data[x]["weather"][0]["id"] < 700:
        send_rain_alert()
        break
