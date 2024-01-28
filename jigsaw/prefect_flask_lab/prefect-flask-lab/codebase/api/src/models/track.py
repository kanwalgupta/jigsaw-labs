from db import find_all, conn, cursor
from datetime import date, timedelta

class Track:
    columns = ['track_id','ranking','date','playlist_id']
    __table__ = 'tracks'

    # @classmethod
    def recent_tracks():

        current_date = date.today()
        one_week_ago = current_date - timedelta(days=7)
        # print(current_date)
        # print(one_week_ago)
        all_tracks = find_all(Track, cursor)
        recent_tracks = []
        for all_track in all_tracks:
            if all_track.date > one_week_ago:
                #print(all_track.date)
                recent_tracks.append(all_track)
        return recent_tracks
            
