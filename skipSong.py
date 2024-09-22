import requests
from pprint import pprint

SPOTIFY_SKIP_TRACK_URL = "https://api.spotify.com/v1/me/player/next"

def skipSong(access_token):
        #Call the url to skip to the next song in queue, Only premium members works tho
        response = requests.post(
        SPOTIFY_SKIP_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
