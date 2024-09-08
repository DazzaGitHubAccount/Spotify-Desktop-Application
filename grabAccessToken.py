import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def grab_access_token():
    #Load the .env file
    load_dotenv()

    #Assing ID, SECRET and URI
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = os.getenv('REDIRECT_URI')

    #Specifying the ID, Secret, URI and Scope
    sp_oauth = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope="user-read-playback-state user-modify-playback-state")

    #Getting the token
    token_info = sp_oauth.get_access_token()

    #Send back the token
    access_token = token_info['access_token']

    return access_token