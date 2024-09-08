import time
import requests
import tkinter as tk

from pprint import pprint
from grabAccessToken import grab_access_token

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
    #Assign the access_token 
    access_token = grab_access_token()
    
    #If there is an access token
    if access_token:
        
        #While it works / is valid
        while True:
            #Get the current track information from the access token
            current_track_info = get_current_track(access_token)

            #If the current track information is correctly assigned
            if current_track_info:
                #Print and apply the gui to it!
                pprint(current_track_info, indent=4)
                gui(current_track_info)
            else:
                print("No track information available.")
        
            #Refresh every 3 seconds
            time.sleep(3)
    else:
         print("Token aquire failed")

if __name__ == '__main__':
    main()