from flask import Flask,render_template,redirect,request
import jinja2
import spotipy
from spotipy.util import oauth2
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth,SpotifyClientCredentials
app = Flask(__name__)

@app.route('/thanks')
def thanks() :
    return render_template('thanks.html')

@app.route('/')
def hello_world():
    SPOTIPY_CLIENT_ID = 'f3425235be384f59a38a3671303c23f8'
    SPOTIPY_CLIENT_SECRET = '17018f06f9c4411297c0bc5956655b24'
    client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
    username='085739657247'
    spotify=spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    scope = 'playlist-modify-public '
    scope += 'user-library-read '
    scope += 'user-follow-read '
    scope += 'user-library-modify '
    scope += 'user-read-private '
    scope += 'user-top-read'
    SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:5000/thanks'
    OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
    OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    cope = 'playlist-modify-public '


    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
    spotify = spotipy.Spotify(auth=token)
    spotify.trace = False
    # oatuh=SpotifyOAuth(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI)
    # spotipy.Spotify.current_user_playlists(oatuh)
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
