from src import *
class Location:
    __table__ = 'locations'
    attributes = ['id', 'longitude', 'latitude', 'address', 
            'zipcode_id', 'venue_id', 'created_at']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def venue(self, cursor):
        query = '''
                SELECT * FROM venues WHERE venues.id = %s
                '''
        cursor.execute(query, (self.venue_id,))
        venue_record = cursor.fetchone()
        return build_from_record(Venue, venue_record)

    def zipcode(self, cursor):
        query = '''
                SELECT * FROM zipcodes WHERE zipcodes.id = %s
                '''
        cursor.execute(query, (self.zipcode_id,))
        zipcode_record = cursor.fetchone()
        return build_from_record(Zipcode, zipcode_record)
