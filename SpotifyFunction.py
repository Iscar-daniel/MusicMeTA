import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth

token=""
def __init__(oauth.spotipy.oauth2.SpotifyOAuth.__) :
    oauth.SpotifyOAuth.__init__(self,client_id, client_secret, redirectUri, None, scope)
    return

def get_token() :
    scope = 'user-library-read'
    username = '085739657247'
    SPOTIPY_CLIENT_ID = 'f3425235be384f59a38a3671303c23f8'
    SPOTIPY_CLIENT_SECRET = '17018f06f9c4411297c0bc5956655b24'
    SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:5000/'
#    credential = test(client_id, client_secret)
    # token = util.prompt_for_user_token(username, scope)
    #token = util.prompt_for_user_token(username, None, client_id, client_secret, redirectUri)
    oauth.SpotifyOAuth.__init__(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,None,scope)
    kode=demiTA.get_access_token()
    return kode


def get_track() :
    token = get_token()
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)