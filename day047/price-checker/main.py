import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 500

url = "https://www.amazon.com/iRobot-Automatic-Disposal-Empties-Allergens-Connected/dp/B085D45SZF/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(id="price_inside_buybox").get_text()
# print(price)
price_without_currency = price.split("$")[1]
# print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(smtp-relay.gmail.com, port=587) as connection:
        connection.starttls()
        result = connection.login(NOPE_EMAIL, NOPE_PASSWORD)
        connection.sendmail(
            from_addr=NOPE_OTHER_EMAIL,
            to_addrs=NOPE_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
