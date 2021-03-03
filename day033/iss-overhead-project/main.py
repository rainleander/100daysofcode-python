import sched
import smtplib
import time
from datetime import datetime
import requests

MY_LAT = 53.173180
MY_LONG = 6.602950

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

s = sched.scheduler(time.time, time.sleep)


# Your position is within +5 or -5 degrees of the ISS position.
def relative_position():
    if MY_LAT - 5 <= iss_longitude <= MY_LAT + 5 or MY_LONG - 5 <= iss_latitude <= MY_LONG +5:
        print("relative_position is True")
        return True
    else:
        print("relative_position is False")
        return False


def is_it_dark():
    if sunset >= time_now >= sunrise:
        print("is_it_dark is True")
        return True
    else:
        print("is_it_dark is False")
        return False


def email_me():
    my_gmail_email = "leanderscode@gmail.com"
    gmail_password = "abcdefg123456789!!"
    gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)

    with gmail_connection as connect:
        connect.starttls()
        connect.login(user=my_gmail_email, password=gmail_password)
        connect.sendmail(
            from_addr=my_gmail_email,
            to_addrs=my_gmail_email,
            msg="Subject:Look UP!\n\nThe ISS is Overhead!"
        )

    print("Email is sent")


def are_we_there_yet(sc):
    print("....are we there yet?")
    if relative_position() and is_it_dark():
        email_me()
    s.enter(15, 1, are_we_there_yet, (sc,))


s.enter(15, 1, are_we_there_yet, (s,))
s.run()
