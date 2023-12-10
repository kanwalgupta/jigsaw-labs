from flask import Flask

@app.route('/parks')
def parks():
    #conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
    conn = psycopg2.connect(database = app.config['DATABASE'])
    cursor = conn.cursor()
    query = '''
            SELECT * FROM parks
            '''
    cursor.execute(query)
    parks = cursor.fetchall()
    return parks

@app.route('/species')
def species():
    #conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
    conn = psycopg2.connect(database = app.config['DATABASE'])
    cursor = conn.cursor()
    query = '''
            SELECT * FROM species
            '''
    cursor.execute(query)
    species = cursor.fetchall()
    return species

@app.route('/species/<id>')
def species_id(id):
    #conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
    conn = psycopg2.connect(database = app.config['DATABASE'])
    cursor = conn.cursor()
    query = '''
            SELECT * 
            FROM species
            WHERE species_id = %s
            '''
    cursor.execute(query, (id,))
    species_id = cursor.fetchall()
    return species_id
    #return id

#return all animals by category within a park
@app.route('/species/<park>/<category>')
def species_by_park_and_category(park,category):
    #conn = psycopg2.connect(database = 'national_parks', user = 'postgres', password = 'postgres')
    conn = psycopg2.connect(database = app.config['DATABASE'])
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
    species_id = cursor.fetchall()
    return species_id
