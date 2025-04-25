from flask import Flask, session, url_for, redirect, request, render_template, jsonify, send_from_directory
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)

client_id = 'b3f60336015b4718a33f1f97f23d4075'
client_secret = '39b23655e0c3458584cee74fab5c889d'
redirect_uri = 'http://127.0.0.1:5000/callback'
scope = 'playlist-read-private'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope,
                        cache_handler=cache_handler)

sp = Spotify(auth_manager=sp_oauth)

@app.route('/')
def home():
    if not sp_oauth.validate_token(sp_oauth.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return render_template('index.html')

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlist'))

@app.route('/get_playlist')
def get_playlist():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        return redirect(sp_oauth.get_authorize_url())
    
    playlists = sp.current_user_playlists()
    playlists_info = [{'name': playlist['name'], 'url': playlist['external_urls']['spotify'], 'images': playlist['images']} for playlist in playlists['items']]
    
    for playlist in playlists_info:
        if playlist['images']:
            sanitized_name = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in playlist['name']).strip().replace(' ', '_').replace('"', '_').replace("'", '_').replace('/', '_').replace('\\', '_')
            image_url = playlist['images'][0]['url']
            image_path = os.path.join('./images', f"{sanitized_name}.jpg")
            if not os.path.exists(image_path):
                response = requests.get(image_url)
                with open(image_path, 'wb') as f:
                    f.write(response.content)
            playlist['images'] = image_path
        else:
            playlist['images'] = None

    return render_template('index.html', playlists=playlists_info)

@app.route('/images')
def get_images():
    images_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
    if not os.path.exists(images_dir):
        return jsonify([])  # Return an empty list if the directory doesn't exist

    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return jsonify(image_files)

@app.route('/logout')
def logout():
    sp_oauth.revoke_token(sp_oauth.get_cached_token())
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)