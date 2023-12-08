import pandas as pd
from src.top_songs import *
from src.song import *
from src.album import *


songs_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-a-data-structures/master/6-top-songs/top-500-songs.txt"
songs_df = pd.read_csv(songs_url, sep='\t', header = None, names = ['rank', 'song', 'artist', 'year'])
songs = songs_df.to_dict('records')

track_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-a-data-structures/master/6-top-songs/track_data.json"
albums_and_tracks = pd.read_json(track_url)
albums_tracks = albums_and_tracks.to_dict('records')

url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-a-data-structures/master/6-top-songs/data.csv"
df = pd.read_csv(url)
albums = df.to_dict('records')

#pet_sounds = albums_tracks[1]
#find_top_songs(pet_sounds, songs)
#print(find_song(songs, "Like a Rolling Stone"))

#find_song(songs, "Like a Rolling Stone")
pet_sounds = albums_tracks[1]
find_top_songs(pet_sounds, songs)