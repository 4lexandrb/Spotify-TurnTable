from flask import render_template, redirect, url_for, request
from . import app
from spotipy import Spotify

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/change_background', methods=['POST'])
def change_background():
    # Logic to change the background image based on user input
    image_url = request.form.get('image_url')
    return redirect(url_for('home', image_url=image_url))

@app.route('/activate_function', methods=['POST'])
def activate_function():
    # Logic to activate a specific function based on user input
    function_name = request.form.get('function_name')
    # Call the appropriate function based on function_name
    return redirect(url_for('home'))