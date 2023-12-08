from src.album import *
from src.song import *

def albums_top_songs(albums_tracks):
    albums_top = {}
    for album in albums_tracks:
        top_songs = find_top_songs(album)
        albums_top[album['album']] = top_songs

    return albums_top

def find_top_songs(album, songs):
    top_songs = [find_song(songs, track)['song']
             for track in tracks(album)
             if find_song(songs, track)]
    uniq_top_songs = list(set(top_songs))
    return uniq_top_songs
