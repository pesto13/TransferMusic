import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os


load_dotenv() # carica le variabili d'ambiente dal file .env
clientid = os.getenv('SPOTIPY_CLIENT_ID') # accede alla variabile d'ambiente MY_TOKEN

secret = os.getenv('SPOTIPY_CLIENT_SECRET')
# Autenticazione all'API di Spotify

# REDIRECT_URI = 'http://localhost:8888/callback'

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid, client_secret=secret, redirect_uri=REDIRECT_URI))

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('pestobellodi')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
