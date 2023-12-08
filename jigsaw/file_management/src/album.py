def songs_from(album):
   return album['tracks']

def tracks(album_track):
    tracks = album_track['tracks']
    return [clean_track(track) for track in tracks]

def clean_track(track):
    return track.split(' - ')[0]
