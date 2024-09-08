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

def gui_labels_update(root, track_label, artist_label, current_track_info):
    #Configure the track label to the current track's name and artist
    track_label.config(text="Track: " + current_track_info["name"])
    artist_label.config(text="Artists: " + current_track_info["artists"])
    root.update()

def gui_update_info(root, track_label, artist_label, access_token):
    
    #Get the current track info
    current_track_info = get_current_track(access_token)

    #If sucessfull, update the terminal with the info and run the update
    if current_track_info:
        pprint(current_track_info, indent=4)
        gui_labels_update(root, track_label, artist_label, current_track_info)
    else:
        print("No track information available")

    #Refresh this every 3 seconds to ensure the song is updated!
    root.after(3000, gui_update_info, root, track_label, artist_label, access_token)

def gui(access_token):
        
        #Create the ui
        root = tk.Tk()
        #Remove the top area of the gui
        root.overrideredirect(True)
        root.attributes('-topmost', True)

        #Track name
        track_label = tk.Label(root, text="Track: ...", )
        track_label.pack(pady=10)

        #Artist name
        artist_label = tk.Label(root, text="Artists: ...",)
        artist_label.pack(pady=10)

        #screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight() 

        window_width = 500  
        window_height = 100

        #Position  
        x_position = screen_width - window_width
        y_position = (screen_height - window_height) - 150

        root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

        #Update the information displayed
        gui_update_info(root, track_label, artist_label, access_token)

        root.mainloop()

def main():
    #Assign the access_token 
    access_token = grab_access_token()
    
    #If there is an access token
    if access_token:
         #Create the GUI!
         gui(access_token)
    else:
         print("Token aquire failed")

if __name__ == '__main__':
    main()