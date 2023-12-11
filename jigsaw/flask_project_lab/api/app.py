from flask import Flask
from settings import DB_NAME, USER, PASSWORD
from api import Park, Species
import psycopg2
import jsonify

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE= DB_NAME
    )

    @app.route('/')
    def index():
        return 'Welcome to the National Parks Database!'

    @app.route('/parks')
    def parks():
        #conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
        conn = psycopg2.connect(database = app.config['DATABASE'])
        cursor = conn.cursor()
        query = '''
                SELECT * FROM parks
                '''
        cursor.execute(query)
        park_records = cursor.fetchall()
        # parks = []
        # for park_record in park_records:
        #     #jsonify(value)
        #     parks.append(Park(park_record))
        # return [park.__dict__ for park in parks]
        return [Park(values = park_record).__dict__ for park_record in park_records]

    @app.route('/species')
    def species():
        conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
        cursor = conn.cursor()
        query = '''
                SELECT * FROM species
                '''
        cursor.execute(query)
        species_records = cursor.fetchall()
        return [Species(values = species_record).__dict__ for species_record in species_records]
        #return species

    @app.route('/species/<id>')
    def species_id(id):
        conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
        cursor = conn.cursor()
        query = '''
                SELECT * 
                FROM species
                WHERE species_id = %s
                '''
        cursor.execute(query, (id,))
        species_id = cursor.fetchall()
        return Species(values = species_id).__dict__
        #return id

    #return all animals by category within a park
    @app.route('/species/<park>/<category>')
    def species_by_park_and_category(park,category):
        conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
        cursor = conn.cursor()
        query = '''
                SELECT s.* 
                FROM parks p
                INNER JOIN species s
                on p.park_code = SUBSTRING(species_id,1,4)
                WHERE 
                park_code = %s
                AND category = %s
                '''
        #SELECT * FROM parks p INNER JOIN species s on p.park_code = SUBSTRING(species_id,1,4) WHERE park_code = 'ACAD' and category = 'Mammal';
        cursor.execute(query, (park,category.title())) #category is title case
        species_records = cursor.fetchall()
        return [Species(values = species_record).__dict__ for species_record in species_records]

    return app
    #look into blueprint to separate out routes into a different file 
    #https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
