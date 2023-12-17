from src import *
class City:
    __table__ = 'cities'
    attributes  = ['id', 'name', 'state_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def state(self, cursor):
        query = '''
                SELECT *
                FROM states
                WHERE states.id = %s
                '''
        cursor.execute(query, (self.state_id,))
        state_record = cursor.fetchone()
        return build_from_record(State, state_record)


