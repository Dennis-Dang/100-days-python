import datetime as dt
import pyinputplus as pyip
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from dotenv import dotenv_values
config = dotenv_values('.env')
CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]

str_date = pyip.inputDatetime("What year do you want to travel to? Type in the date in this format YYYY-MM-DD: ",
                              formats=('%Y-%m-%d',))
date = str_date.date()

while date > dt.datetime.today().date():
    print(f"This is a date in the future, songs are not created yet for this date!\n"
          f"Enter a date before or on {dt.datetime.today().strftime('%Y-%m-%d')}.")
    str_date = pyip.inputDatetime("What year do you want to travel to? Type in the date in this format YYYY-MM-DD: ",
                                  formats=('%Y-%m-%d',))
    date = str_date.date()

hot_100 = requests.get(f"https://www.billboard.com/charts/hot-100/{str_date.strftime('%Y-%m-%d')}")
hot_100.raise_for_status()
# Remember to wait for 5 secs between requests.
# with open('website.htm', encoding='utf-8') as file:
#     web_doc = file.read()
songs = BeautifulSoup(hot_100.text, features="html.parser")
# songs = BeautifulSoup(web_doc, features="html.parser")
song_list = songs.findAll('div', class_='o-chart-results-list-row-container')
song_titles = []
song_artists = []
for song in song_list:
    h3_element = song.select_one('h3', id='title-of-a-story')  # Find the first H3 element with the specified class
    if h3_element:
        h3_title = h3_element.getText(strip=True)  # Extract the text content of the H3 element
        song_titles.append(h3_title)
        span_element = h3_element.find_next_sibling('span')  # Find the following span element
        if span_element:
            span_text = span_element.getText(strip=True).split()[0]  # Extract the text content of the span element
            song_artists.append(span_text)

print(song_titles)
print(song_artists)
spotify = spotipy.Spotify(
    # Authorization Code Flow for Spotify’s OAuth
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        show_dialog=True, # Show authorization dialog every time when authenticating regardless refresh token available
        cache_path="token.txt",
        scope="playlist-modify-private"
    )
)

user_id = spotify.current_user()["id"]
print(user_id)

track_uris = []
not_found = []
for idx in range(100):
    result = spotify.search(q=f"{song_titles[idx]} artist: {song_artists[idx]} year:{str_date.strftime('%Y')}",
                            limit=1, type="track", market="US")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song_titles[idx]} doesn't exist in spotify.")
        not_found.append(song_titles[idx])
    else:
        print(uri)
        track_uris.append(uri)
    if idx % 10 == 0:
        sleep(1) # wait a second for every 10 requests.

playlist = spotify.user_playlist_create(
    user=user_id,
    name=f"{str_date.strftime('%Y-%m-%d')} Billboard 100",
    public=False,
    description="A playlist created by ThrowbackMaker"
)

spotify.playlist_add_items(
    playlist_id=playlist["id"],
    items=track_uris
)

print("Your playlist is complete\nThe following songs could not be found on spotify: ")
for song in not_found:
    print(song)
print(f"Link: https://open.spotify.com/playlist/{playlist['id']}")
