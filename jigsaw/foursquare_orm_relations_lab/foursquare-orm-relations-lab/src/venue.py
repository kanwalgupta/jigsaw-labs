import src
class Venue():
    __table__ = 'venues'
    attributes = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def find_by_foursquare_id(self, foursquare_id, cursor):
        foursquare_query = """SELECT * FROM venues WHERE foursquare_id = %s"""
        cursor.execute(foursquare_query, (foursquare_id,))
        record = cursor.fetchone()
        return src.build_from_record(src.Venue, record)

    def location(self, cursor):
        query = '''
                SELECT * FROM locations WHERE locations.venue_id = %s 
                '''
        cursor.execute(query, (self.id,))
        location_record = cursor.fetchone()
        #breakpoint()
        return src.build_from_record(src.Location, location_record)
        
