from api.lib.orm import build_from_record, find
from api.lib.db import save
from api.models.address import Address

class Person:
    __table__ = 'person.person'
    columns = ['businessentityid', 'persontype', 'namestyle', 'title', 'firstname',
      'middlename', 'lastname', 'suffix', 'emailpromotion', 
      'additionalcontactinfo', 'demographics', 'rowguid', 'modifieddata']
    
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        self.__dict__ = kwargs

    @classmethod
    def find_or_create_by_first_last_name_and_id(cls, firstname, lastname, businessentityid, conn):
        cursor = conn.cursor()
        person = find(cursor, Person, businessentityid)
        #maybe there's a better way than checking for a null db record, then a NoneType object
        if person is None:
            new_person = cls(firstname = firstname, lastname = lastname, businessentityid = businessentityid)
            return save(new_person, conn, cursor)
        elif person.firstname == firstname and person.lastname == lastname and person.businessentityid == businessentityid:
            return person

    #method to return all addresses for given businessentityid 
    def addresses(self, conn):
        cursor = conn.cursor()
        query = f'''
                SELECT *
                FROM person.address a
                   INNER JOIN person.businessentityaddress b
                   ON a.addressid = b.addressid
                WHERE b.businessentityid = %s
                '''
        cursor.execute(query, (self.businessentityid,))
        address_records = cursor.fetchall()
        return [build_from_record(Address, address_record) for address_record in address_records]
        
    
    def to_json(self, conn):
        addresses = self.addresses(conn)
        addresses_json = [address.__dict__ for address in addresses]
        person_dict = self.__dict__
        person_dict['addresses'] = addresses_json
        return person_dict
        #could've combined this with the addresses method to make things simpler
        
       
             

    