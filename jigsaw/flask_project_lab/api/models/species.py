class Species():
    __table__ = 'species'
    columns = ['species_id','park_name','category','order','family','scientific_name','common_names','record_status','occurrence','nativeness','abundance','seasonality','conservation_status']

    def __init__(self,values):
        self.__dict__ = dict(zip(self.columns, values))
    
