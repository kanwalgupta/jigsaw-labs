def find_by_artist(songs: list, artist_name: str) -> list:
    found_songs = []
    for song in songs:
        if song['artist'] == artist_name:
            found_songs.append(song)
    return found_songs

def display_song_names(songs:list) -> list:
    return [song['song'] for song in songs]

def alphabetize(songs:list) -> list:
    alphabetized = sorted(songs, key = lambda x:x['song'])
    return alphabetized