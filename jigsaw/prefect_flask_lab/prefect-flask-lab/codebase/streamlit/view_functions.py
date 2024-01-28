import requests

ROOT_URL = 'http://127.0.0.1:5000'
TRACKS_URL = f"{ROOT_URL}/tracks"

def get_tracks():
    response = requests.get(TRACKS_URL)
    return response.json()