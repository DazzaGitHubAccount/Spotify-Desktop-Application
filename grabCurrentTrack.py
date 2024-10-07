import requests
from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
    #Request for the current track using the URL + access token
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    #Check if there was a response
    if response.status_code != 200:
         print(f"Error: {response.status_code}, {response.text}")
         return None
    
    resp_json = response.json()

    #Check if there isn't an item
    if 'item' not in resp_json:
         print("No current track found")
         pprint(resp_json)
         return None

    #Grab the Track ID, Name, Artist and if there are many artists
    track_ID = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artists['name'] for artists in artists]
    )

    #Link to the track (Not sure if will be needed later)
    link = resp_json['item']['external_urls']['spotify']

    #Store information     
    track_info = {
        "id": track_ID,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    #Return the info, end of function
    return track_info
