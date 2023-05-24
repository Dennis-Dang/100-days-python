import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

movies = BeautifulSoup(response.text, features="html.parser")
all_movies = movies.findAll(name="h3", attrs={"class": "title"})

rankings_movies = [movie.text+'\n' for movie in all_movies]
rankings_movies.reverse()

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.writelines(rankings_movies)

