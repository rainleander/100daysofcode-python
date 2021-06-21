from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

SPOTIPY_CLIENT_ID = "NOPE"
SPOTIPY_CLIENT_SECRET = "NOPE"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
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

song_uris = []
year = time_travel.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{time_travel} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
