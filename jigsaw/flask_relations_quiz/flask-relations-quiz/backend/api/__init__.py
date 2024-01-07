from flask import Flask, jsonify
from api.lib.orm import find_all, build_from_record, find
from api.lib.db import get_db
from api.models.person import Person
from api.models.address import Address
from api.models.business_entity_address import BusinessEntityAddress

import json
import psycopg2

def create_app(db_name):
    app = Flask(__name__)
    app.config.from_mapping(DATABASE = db_name)

    #conn = psycopg2.connect(dbname = db_name)

    @app.route("/")
    def root():
        return "welcome to the adventureworks app"

    @app.route("/persons")
    def persons():
        conn = get_db()
        cursor = conn.cursor()
        persons = find_all(cursor, Person)
        person_dicts = [person.__dict__ for person in persons]
        return jsonify(person_dicts)
        #return response
        #return jsonify(person_dicts) fix this later
    
    @app.route("/persons/lastname/<lastname>")
    def persons_last_name(lastname):
        conn = get_db()
        cursor = conn.cursor()
        # get size of person table
        cursor.execute('SELECT COUNT(*) FROM person.person')
        person_count = cursor.fetchone()
        #print(person_count)
        persons = find_all(cursor, Person, person_count)
        #print(len(persons))
        selected_persons = []
        for person in persons:
            if person.lastname == lastname:
                selected_persons.append(person)
        last_name_dicts = [selected_person.__dict__ for selected_person in selected_persons]
        return jsonify(last_name_dicts)
    
    @app.route("/addresses")
    def addresses():
        conn = get_db()
        cursor = conn.cursor()
        addresses = find_all(cursor, Address)
        address_dicts = [address.__dict__ for address in addresses]
        return jsonify(address_dicts)

    @app.route("/person/addresses/<businessentityid>")
    def person_address(businessentityid):
        conn = get_db()
        cursor = conn.cursor()
        person = find(cursor, Person, businessentityid)
        return person.to_json(conn)
        
    return app
