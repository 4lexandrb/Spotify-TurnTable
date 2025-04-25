import os

from flask import Flask, session, url_for, redirect, request
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
import requests

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(64)
app.secret_key = os.urandom(64)

client_id = 'b3f60336015b4718a33f1f97f23d4075'
client_secret = '39b23655e0c3458584cee74fab5c889d'
redirect_uri = 'http://127.0.0.1:5000/callback'
scope = 'playlist-read-private'

auth_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
api_base_url = 'https://api.spotify.com/v1/'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope,
                        cache_handler=cache_handler,
                        show_dialog=False
                        )

sp = Spotify(auth_manager=sp_oauth)


@app.route('/')
def home():
    if not sp_oauth.validate_token(sp_oauth.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please navigate here: {auth_url}")
        return redirect(auth_url)
    return redirect(url_for('get_playlist'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlist'))

@app.route('/get_playlist')
def get_playlist():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):   # check if user is authenticated (token is valid)
        return redirect(sp_oauth.get_authorize_url())
    
    playlists = sp.current_user_playlists()
    playlists_info = [(playlist['name'], playlist['external_urls']['spotify'], playlist['images']) for playlist in playlists['items']]
    # playlists_html = [f'{name}: {url}' for name, url in playlists_info]
    # '<br>'.join(playlists_html)

    # Ensure the 'images' folder exists
    os.makedirs('images', exist_ok=True)

    for name, url, image in playlists_info:
        if image:
            sanitized_name = name.replace('"', '').replace("'", '').replace('/', '_').replace('\\', '_')
            image_url = image[0]['url']
            response = requests.get(image_url)
            if response.status_code == 200:
                
                with open(f'images/{sanitized_name}.jpg', 'wb') as img_file:
                    img_file.write(response.content)

    return playlists_info

@app.route('/logout')
def logout():
    sp_oauth.revoke_token(sp_oauth.get_cached_token())
    session.clear()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)