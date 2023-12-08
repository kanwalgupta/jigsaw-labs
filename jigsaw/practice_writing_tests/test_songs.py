from songs import *

songs = [{'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965},  
         {'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965},
         {'rank': 5, 'song': 'Respect', 'artist': 'Aretha Franklin', 'year': 1967}]

def test_find_by_artist():
    found_songs = find_by_artist(songs, 'The Rolling Stones')
    assert found_songs == [{'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965}]

def test_find_by_artist_none():
    found_songs = None
    assert found_songs == None

def test_display_song_names():
    found_names = display_song_names(songs)
    assert found_names == ['Like a Rolling Stone','Satisfaction','Respect']
    #assert found_names == ['Like a Rolling Stone','Respect','Satisfaction']

def test_alphabetize():
    sorted_songs = alphabetize(songs)
    assert sorted_songs == [{'rank': 1, 'song': 'Like a Rolling Stone', 'artist': 'Bob Dylan', 'year': 1965},  
         {'rank': 5, 'song': 'Respect', 'artist': 'Aretha Franklin', 'year': 1967},
         {'rank': 2, 'song': 'Satisfaction', 'artist': 'The Rolling Stones', 'year': 1965}]




