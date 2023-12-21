CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    teacher_name VARCHAR(255) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    teacher_id INTEGER REFERENCES teachers (id) ON DELETE CASCADE
);

CREATE TABLE seats (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses (id) ON DELETE CASCADE,
    student_id INTEGER REFERENCES students (id) ON DELETE CASCADE
);

\copy teachers(id, teacher_name) FROM './data/teachers.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')

\copy students(id, student_name) FROM './data/students.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')

\copy courses(id, course_name, teacher_id) FROM './data/courses.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')

\copy seats(id, course_id, student_id) FROM './data/seats.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')