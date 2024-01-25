import os
from datetime import date
from spotify_extractor.spotify_client import build_client
import pandas as pd


def get_playlist_tracks(playlist_id):
    client = build_client()
    tracks = client.playlist_items(playlist_id)
    return tracks['items']

def extract_tracks_info(tracks, playlist_id):
    #selected_attributes = ['playlist_id','current_date','track_id','ranking']
    tracks_info = []
    # for track in tracks:
    #     extracted_track_info = {}
    #     for k,v in track.items():
    #         if k in selected_attributes:
    #             extracted_track_info[k] = v
    #     tracks_info.append(extracted_track_info)
    #for track in tracks:
    for index in range(len(tracks)):
        extracted = {}
        extracted['track_id'] = tracks[index]['track']['id']
        extracted['ranking'] = index + 1
        extracted['date'] = date.today()
        extracted['playlist_id'] = playlist_id
        tracks_info.append(extracted)
    return tracks_info
  


def write_to_csv(tracks):
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    tracks_df = pd.DataFrame(tracks)
    data_path = "./data/track_listings.csv"
    tracks_df.to_csv(data_path)