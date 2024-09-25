import tkinter as tk
import threading

from pprint import pprint
from grabCurrentTrack import get_current_track

from skipSong import skipSong

#Check if the track is already updating
track_update_indicator = False

def display_animated_gif(root, gif_holder, gif_path, frame_count):
    #Rendering the gif Reference: https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter
    frames = [tk.PhotoImage(file=gif_path, format='gif -index %i' % i) for i in range(frame_count)]

    def update(ind):
        frame = frames[ind]
        gif_holder.configure(image=frame)
        ind += 1
        if ind >= frame_count:
            ind = 0
            #When the gif finishes, loop it 
            root.after(10, update, ind)  
        else:
            root.after(50, update, ind)
    update(0) 

def gui_labels_update(root, track_label, artist_label, current_track_info):

    #Configure the track label to the current track's name and artist
    track_label.config(text="Track: " + current_track_info["name"])
    artist_label.config(text="Artists: " + current_track_info["artists"])

    root.update()

def gui_update_info(root, track_label, artist_label, access_token):


    #Use a thread to get the info!
    def get_track_info():
        current_track_info = get_current_track(access_token)
        if current_track_info:
            pprint(current_track_info, indent=4)
            root.after(0, gui_labels_update, root, track_label, artist_label, current_track_info)
        else:
            print("No track information available")

    #Start the thread
    threading.Thread(target=get_track_info).start()

    #Refresh this every 3 seconds to ensure the song is updated!
    root.after(3000, gui_update_info, root, track_label, artist_label, access_token)

def skip_button_pressed(root, track_label, artist_label, access_token):

    def skip_update():
        skipSong(access_token)
        gui_update_info(root, track_label, artist_label, access_token)
        
    threading.Thread(target=skip_update).start()

def gui(access_token):
        
    #Create the ui
    root = tk.Tk()
    #Remove the top area of the gui
    #root.overrideredirect(True)
    root.attributes('-topmost', True)

    #Gif holder
    gif_holder = tk.Label(root)
    gif_holder.pack(side=tk.LEFT)

    #Gif on the left side
    gif_path = "vibin.gif" 
    frame_count = 151
    display_animated_gif(root, gif_holder, gif_path, frame_count)

    #Track name
    track_label = tk.Label(root, text="Track: ...", )
    track_label.pack(pady=10)

    #Artist name
    artist_label = tk.Label(root, text="Artists: ...",)
    artist_label.pack(pady=10)

    #Skip song button + update track info
    button = tk.Button(root, text="Skip Song", command=lambda: skip_button_pressed(root, track_label, artist_label, access_token))
    button.pack(pady=10)

    #Screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 

    window_width = 500  
    window_height = 200

    #Position  
    x_position = screen_width - window_width
    y_position = (screen_height - window_height) - 150

    root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    #Update the information displayed
    gui_update_info(root, track_label, artist_label, access_token)

    root.mainloop()
