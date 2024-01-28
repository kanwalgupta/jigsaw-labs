from flask import Flask
from db import find_all, conn, cursor
from src.models.track import Track
import psycopg2


def create_app():
    app = Flask(__name__)

    # conn = psycopg2.connect(database = "spotify_top_songs")
    # cursor = conn.cursor()

    @app.route('/')
    def index():
        return "Welcome to Spotify Tracker"
    
    @app.route('/tracks')
    def tracks():
        tracks = find_all(Track, cursor)
        return [track.__dict__ for track in tracks]
    
    @app.route('/recent_tracks')
    def recent_tracks():
        recent_tracks = Track.recent_tracks()
        return [recent_track.__dict__ for recent_track in recent_tracks]

    return app
