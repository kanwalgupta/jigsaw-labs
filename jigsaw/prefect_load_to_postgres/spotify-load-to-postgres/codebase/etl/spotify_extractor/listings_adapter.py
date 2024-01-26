import os
from datetime import date

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from db import engine
from etl.spotify_extractor.spotify_client import client


def get_playlist_tracks(playlist_id):
    playlist = client.playlist_items(playlist_id)
    tracks = playlist['items']
    return tracks

def extract_tracks_info(tracks, playlist_id):
    selected_tracks = []
    current_date = str(date.today())
    for idx, track in enumerate(tracks):
        track_id = track['track']['id']
        ranking = idx + 1
        selected_track = {'track_id': track_id,
                          'ranking': ranking,
                          'date': current_date,
                          'playlist_id': playlist_id
                          }
        selected_tracks.append(selected_track)
    return selected_tracks

def write_to_csv(tracks):
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    tracks_df = pd.DataFrame(tracks)
    #data_path = f"./data/track-listings.csv"
    #append date to the front of path
    current_date = date.today()
    data_path = f"./data/{current_date}-track-listings.csv"
    tracks_df.to_csv(data_path)

def find_recent_files(engine):
    # pass
    # use read_sql function to find the most recent date that we loaded data into db
    # return file names after that date
    query = '''
            SELECT MAX(date) FROM tracks
            '''
    df = read_sql(query, engine)
    most_recent_date = df.at[0, 'max']
    recent_files = []
    file_path = './data'
    filenames = os.listdir(file_path)
    for filename in filenames:
        file_date = filename[:10]
        print(file_date)
        if file_date > str(most_recent_date):
            recent_files.append(filename)
    return recent_files        


def load_files_to_postgres():
    recent_files = find_recent_files(engine)
    dfs = [pd.read_csv(f'./data/{recent_file}', index_col = 0) for recent_file in recent_files]
    
    for df in dfs:
        load_to_postgres(df, engine)
        

def load_to_postgres(df, engine, table_name = 'tracks'):
    df.to_sql(table_name, engine, if_exists='append', index=False)

def read_sql(query, engine):
    df = pd.DataFrame(engine.connect().execute(text(query)))
    return df
    
    