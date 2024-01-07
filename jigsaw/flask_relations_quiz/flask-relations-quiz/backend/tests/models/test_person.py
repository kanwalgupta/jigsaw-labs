from api.models.person import Person
from api.models.address import Address
from api.models.business_entity_address import BusinessEntityAddress
from api.lib.db import save, test_cursor, test_conn, drop_records, drop_table_records, save_address
import pytest

def build_records(conn, cursor):
    for i in range(1, 3):
        sam = Person(firstname =f'Sam {i}', lastname = 'ok', businessentityid = i, persontype = 'EM')
        save(sam, conn, cursor)

@pytest.fixture()
def build_people():
    
    drop_records(test_cursor, test_conn, 'person.person')
    build_records(test_conn, test_cursor)

    yield

    drop_records(test_cursor, test_conn, 'person.person')

@pytest.fixture()
def build_person_address():

    drop_records(test_cursor, test_conn, 'person.person')
    #build_records(test_conn, test_cursor)
    person1 = Person(firstname = 'Sam 1', lastname = 'ok', businessentityid = 1)
    saved_person1 = save(person1, test_conn,test_cursor)

    address1 = Address(addressid = 1,addressline1 = '123 romeo',
                    addressline2 = 'earth', city= 'nyc', stateprovinceid = 12, postalcode = 11231,
            spatiallocation = 'ok')
    saved_address1 = save_address(address1, test_conn, test_cursor)

    address2 = Address(addressid = 2,addressline1 = '456 juliett',
                    addressline2 = 'earth', city= 'nyc east', stateprovinceid = 12, 
                    postalcode = 11231, spatiallocation = 'ok')
    saved_address2 = save_address(address2, test_conn, test_cursor)

    business_entity_address1 = BusinessEntityAddress(addressid = 1, businessentityid = 1, addresstypeid = 1)
    save(business_entity_address1, test_conn, test_cursor)

    business_entity_address1 = BusinessEntityAddress(addressid = 2, businessentityid = 1, addresstypeid = 2)
    save(business_entity_address1, test_conn, test_cursor)

    yield

    drop_table_records(['person.person','person.address','person.businessentityaddress'],test_cursor, test_conn)

def test_person_accepts_mass_assignment():
    person = Person(persontype = 'EM', namestyle = 'f', 
                    firstname = 'Ken', middlename = 'J', lastname = 'Sanchez')
    assert person.firstname == 'Ken'

def test_person_has_property_of__table__():
    assert Person.__table__ == 'person.person'

def test_person_has_property_of_columns():
    assert Person.columns == ['businessentityid', 'persontype', 'namestyle', 'title', 'firstname',
      'middlename', 'lastname', 'suffix', 'emailpromotion', 
      'additionalcontactinfo', 'demographics', 'rowguid', 'modifieddata']
     
def test_find_or_create_by_first_and_last_name_finds_the_related_person_if_already_in_the_database(build_people):
    person = Person.find_or_create_by_first_last_name_and_id(firstname = 'Sam 1', lastname = 'ok', businessentityid = 1, conn = test_conn)
    assert person.firstname == 'Sam 1'
    assert person.businessentityid == 1
    test_cursor.execute('select count(*) from person.person')
    num_records = test_cursor.fetchone()
    assert num_records == (2,)

def test_find_or_create_by_first_and_last_name_creates_a_new_person_when_not_in_db(build_people):
    person = Person.find_or_create_by_first_last_name_and_id(firstname = 'Sam 10', lastname = 'ok', 
                                                             businessentityid = 3, conn = test_conn)
    assert person.firstname == 'Sam 10'
    assert person.lastname == 'ok'    
    test_cursor.execute('select count(*) from person.person')
    num_records = test_cursor.fetchone()
    assert num_records == (3,)

def test_find_person_addresses(build_person_address):
    person1 = Person(firstname = 'Sam 1', lastname = 'ok', businessentityid = 1)
    addresses = person1.addresses(test_conn)
    #assert addresses[0]['addressid'] == 1
    assert addresses[0].addressid == 1



