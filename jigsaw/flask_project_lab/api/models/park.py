class Park():
    __table__ = 'parks'
    columns = ['park_code','park_name','state','acres','latitude','longitude']
    
    def __init__(self,values):
        self.__dict__ = dict(zip(self.columns, values))