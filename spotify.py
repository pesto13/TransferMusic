import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os


load_dotenv() # carica le variabili d'ambiente dal file .env
clientid = os.getenv('SPOTIPY_CLIENT_ID') # accede alla variabile d'ambiente MY_TOKEN

secret = os.getenv('SPOTIPY_CLIENT_SECRET')
# Autenticazione all'API di Spotify

REDIRECT_URI = 'http://localhost:8888/callback'

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid, client_secret=secret, redirect_uri=REDIRECT_URI))

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri=REDIRECT_URI))


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)



zz = sp.search('emberassed', limit=1, type='track')
damn = zz['tracks']['items'][0]['uri']

print(damn)

# da quello che ho capito devo mettere URI altrimenti non posso fare il login :D
print(sp.current_user())

""" playlist = sp.user_playlist_create(user=sp.current_user()['id'], name='AAA')

# Aggiungi le canzoni alla playlist
sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=playlist['id'], tracks=damn) """

print(f"Playlist creata con successo!")