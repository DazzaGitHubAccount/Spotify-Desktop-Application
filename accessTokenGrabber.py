import time
import requests
import tkinter as tk

from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = 'BQC1EEtrc6i8LYIUUI1h-KK1EEdgn6xy8eO-KZxp15YpuDGRn-G2NovyiYvZNRupcrmnL1CZmBcPfiKBSILpyUhXTJgRp25bRrBUhHcusB8nZ1WtkHO7ecgXONVkmhuOlReLZQFYd-KuCZjBdIgoSyy0mQcrpbAmvKbUp8FCUHgJo8ZLOmaYS3V0FpE1fmSCoBwhCr8Dgfiz_M_Onx70QxAE91raLbH_miVB6HF5EAxCedxnYSwEyg5qZkgg8DlwK9dPO6ijtuWmnQh_F604Ei-U2Lh5lxj23VTgGq8-GU2dfg3BHoAw_QMAY-mbG4XPM44kSbBnpCh5w6JIj9W9O4xO_MKP'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

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
    while True:
        current_track_info = get_current_track(
            SPOTIFY_ACCESS_TOKEN
        )

        pprint(current_track_info, indent = 4)
        gui(current_track_info)

        time.sleep(3)

if __name__ == '__main__':
    main()