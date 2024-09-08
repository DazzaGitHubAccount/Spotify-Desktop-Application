import time
import requests
import tkinter as tk

from pprint import pprint
from grabAccessToken import grab_access_token

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    # Check if there was a response
    if response.status_code != 200:
         print(f"Error: {response.status_code}, {response.text}")
         return None
    
    resp_json = response.json()


    if 'item' not in resp_json:
         print("No current track found")
         pprint(resp_json)
         return None

    track_ID = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artists['name'] for artists in artists]
    )

    link = resp_json['item']['external_urls']['spotify']
    
    track_info = {
        "id": track_ID,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    return track_info

def gui(current_track_info):
        
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes('-topmost', True)

        track_label = tk.Label(root, text="Track: " + current_track_info["name"])
        track_label.pack(pady=10)

        artist_label = tk.Label(root, text="Artists: " + current_track_info["artists"])
        artist_label.pack(pady=10)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() 

        window_width = 500  
        window_height = 100  
        x_position = screen_width - window_width
        y_position = (screen_height - window_height) - 150

        root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        root.mainloop()

def main():
    access_token = grab_access_token()
    
    if access_token:
        while True:
            current_track_info = get_current_track(access_token)

            if current_track_info:
                pprint(current_track_info, indent=4)
                gui(current_track_info)
            else:
                print("No track information available.")
        
            time.sleep(3)
    else:
         print("Token aquire failed")

if __name__ == '__main__':
    main()