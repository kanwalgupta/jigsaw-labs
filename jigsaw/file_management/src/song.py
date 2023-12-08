def find_song(songs, name):
    found_song = [song for song in songs if song['song'] == name]
    return next(iter(found_song), None)
