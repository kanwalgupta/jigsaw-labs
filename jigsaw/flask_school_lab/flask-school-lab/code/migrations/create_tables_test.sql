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