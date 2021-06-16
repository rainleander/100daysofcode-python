from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

time_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}{time_travel}")
top_100 = response.text

soup = BeautifulSoup(top_100, "html.parser")

songs = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
song_list = []

for song in songs:
    title = song.getText()
    song_list.append(title)

print(song_list)
