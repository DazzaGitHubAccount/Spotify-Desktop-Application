import tkinter as tk

from pprint import pprint
from grabCurrentTrack import get_current_track

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