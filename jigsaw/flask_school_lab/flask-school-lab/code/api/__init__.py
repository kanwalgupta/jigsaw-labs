from flask import Flask
from api.lib.db import find, find_all, build_from_record, build_from_records
from api.models.teacher import Teacher
import psycopg2
import jsonify

def create_app(db):
    app = Flask(__name__)

    conn = psycopg2.connect(database=db)

    @app.route("/")
    def index():
        return "Welcome to the Schools API"
    
    @app.route("/teachers")
    def teachers():
        records = find_all(Teacher, conn)
        return build_from_records(Teacher, records)
        # cursor = conn.cursor()
        # query = '''
        #         SELECT *
        #         FROM teachers
        #         '''
        # cursor.execute(query)
        # teacher_records = cursor.fetchall()
        # return teacher_records
    
    @app.route("/teachers/<id>")
    def teacher(id):
        record = find(Teacher, id, conn)
        return build_from_record(Teacher, record)
        # cursor = conn.cursor()
        # query = '''
        #         SELECT *
        #         FROM teachers t
        #         WHERE t.id = %s
        #         '''
        # cursor.execute(query,(id,))
        # teacher_record = cursor.fetchall()
        # #teacher_json = jsonify(teacher_record)
        # return teacher_record
    return app