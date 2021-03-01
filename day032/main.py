# ----- SmtpLib Notes ----- #
# import smtplib
#
# my_gmail_email = "leanderscode@gmail.com"
# gmail_password = "abcdefg123456789!!"
# gmail_connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# my_yahoo_email = "leanderscode@yahoo.com"
# yahoo_password = "mkmpusprtagcolim"
# yahoo_connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
#
# # connection.starttls()
# # connection.login(user=my_gmail_email, password=gmail_password)
# # connection.sendmail(from_addr=my_gmail_email,
# #                     to_addrs=my_yahoo_email,
# #                     msg="Subject:Hello and Test\n\nThis is the body of my email and how awesome is this?!?")
# # connection.close()
#
# special_message = """
#     Subject:Once More With Feeling\n\nOnce More, with Feeling is the seventh episode of the sixth season\n
#     of the supernatural drama television series Buffy the Vampire Slayer (1997–2003) and the only one in\n
#     the series performed as a musical.
#     """
#
# # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
# #     connection.starttls()
# #     connection.login(user=my_gmail_email, password=gmail_password)
# #     connection.sendmail(
# #         from_addr=my_gmail_email,
# #         to_addrs=my_yahoo_email,
# #         msg="Subject:Connection Test\n\nThis is the body of my email and how awesome is this?!?"
# #     )
#
# with yahoo_connection as connection:
#     connection.starttls()
#     connection.login(user=my_yahoo_email, password=yahoo_password)
#     connection.sendmail(
#         from_addr=my_yahoo_email,
#         to_addrs=my_gmail_email,
#         msg="Subject:Yahoo Test\n\nThis is the body of my email and how awesome is this?!?"
#     )

# # ----- DateTime Notes ----- #
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# if year == 2021:
#     print("Wear a face mask, damnit.")
# print(year)
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1976, month=5, day=24)
# print(date_of_birth)

# ----- Motivational Quotes Challenge ----- # 
import datetime as dt
import smtplib

def send_email():
    
