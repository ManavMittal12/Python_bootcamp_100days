import requests
import requests_cache
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import os

requests_cache.install_cache("Songs_list")

if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

# get date from the user
date_of_search : str = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD:\n")


response = requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date_of_search}/")
soup = BeautifulSoup(response.text, "html.parser")


songs_element = soup.find_all(name="h3", class_="chart-entry__title")
names_of_songs = [song.get_text().strip() for song in songs_element]
print(names_of_songs)

PLAYLIST_NAME = f"{date_of_search} Billboard 100"

yt = YTMusic("browser.json")
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

# Creating a playlist
for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break
    else:
        playlist_id = yt.create_playlist(
            title=PLAYLIST_NAME,
            description="Top 100 songs from the time machine.",
            privacy_status="PRIVATE"
        )
        print("Playlist_Created.")
        break



# Search the song
for song in names_of_songs:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id,[search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reasons {e}")
