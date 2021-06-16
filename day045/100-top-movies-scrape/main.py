from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_site = response.text

soup = BeautifulSoup(empire_site, "html.parser")

all_movies = soup.find_all(name="titleText")

# movies_list = []
#
# movies = soup.find_all(name="h3")
#
# for x in movies:
#     movie = x.getText()
#     movies_list.append(movie)

print(all_movies)
