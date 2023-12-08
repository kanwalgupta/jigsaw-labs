import psycopg2

conn = psycopg2.connect(dbname="movies", user="postgres", password="postgres", host="localhost", port="5432")

cursor = conn.cursor()

def find_all():
    cursor.execute("SELECT * FROM movies;")
    movies = cursor.fetchall()
    return movies

#print(find_all())

cursor.execute("INSERT INTO movies (name,genre) VALUES ('Fast 5', 'Action');")
cursor.commit()