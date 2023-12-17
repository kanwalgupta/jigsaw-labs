import src
class Zipcode:
    __table__ = 'zipcodes'
    attributes = ['id', 'code', 'city_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def city(self, cursor):
        query = '''
                SELECT * FROM cities WHERE cities.id = %s
                '''
        cursor.execute(query,(self.city_id,))
        city_record = cursor.fetchone()
        return src.build_from_record(src.City, city_record)

    def locations(self, cursor):
        query = '''
                SELECT DISTINCT locations.*
                FROM locations
                  INNER JOIN zipcodes
                  ON locations.zipcode_id = zipcodes.id
                WHERE locations.zipcode_id = %s
                '''
        cursor.execute(query, (self.id,))
        location_records = cursor.fetchall()
        return src.build_from_records(src.Location, location_records)
