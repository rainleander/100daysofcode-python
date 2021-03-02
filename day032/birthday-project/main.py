import datetime as dt
import pandas
import random
import smtplib

today_today = dt.datetime.today()
today_month = today_today.month
today_day = today_today.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]
    birthday_person_name = birthday_person["name"]
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        message = file.read()
        message_body = message.replace("[NAME]", birthday_person_name)

    my_gmail_email = "leanderscode@gmail.com"
    gmail_password = "abcdefg123456789!!"
    gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    
    birthday_person_email = birthday_person["email"]

    with gmail_connection as connect:
        connect.starttls()
        connect.login(user=my_gmail_email, password=gmail_password)
        connect.sendmail(
            from_addr=my_gmail_email,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday\n\n{message_body}"
        )

    print(f"Sent a happy birthday message to {birthday_person_name}!")
