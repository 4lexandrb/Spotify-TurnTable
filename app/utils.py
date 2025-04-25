def get_playlist_images(playlists_info):
    images = []
    for playlist in playlists_info:
        # Assuming each playlist has an 'images' key with a list of image URLs
        if 'images' in playlist and playlist['images']:
            images.append(playlist['images'][0]['url'])  # Get the first image URL
    return images

def get_random_image(images):
    import random
    return random.choice(images) if images else None

def fetch_playlist_data(sp):
    playlists = sp.current_user_playlists()
    return playlists['items'] if playlists and 'items' in playlists else []