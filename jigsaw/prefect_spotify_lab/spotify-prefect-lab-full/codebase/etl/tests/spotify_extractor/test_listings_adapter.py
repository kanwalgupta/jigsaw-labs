from spotify_extractor.listings_adapter import (extract_tracks_info,
                                                get_playlist_tracks)
from tests.spotify_extractor.data import tracks


def test_get_playlist_tracks():
    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    tracks = get_playlist_tracks(playlist_id)
    assert len(tracks) == 50
    item_keys = list(tracks[0].keys())
    assert item_keys == ['added_at', 'added_by',
     'is_local', 'primary_color', 'track', 'video_thumbnail']

def test_extract_tracks():
    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    selected_tracks = extract_tracks_info(tracks, playlist_id)
    first_track = selected_tracks[0]
    assert list(first_track.keys()) == ['track_id', 'ranking', 'date', 'playlist_id']
    assert first_track['track_id'] == '3IX0yuEVvDbnqUwMBB3ouC'
    assert first_track['ranking'] == 1
    assert first_track['playlist_id'] == '37i9dQZEVXbLRQDuF5jeBp'