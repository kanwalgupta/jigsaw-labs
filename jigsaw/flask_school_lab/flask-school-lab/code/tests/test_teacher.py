import pytest, psycopg2
from api.models.teacher import Teacher
from api.lib.db import save, clear_table
from settings import TEST_DATABASE

conn = psycopg2.connect(database=TEST_DATABASE)

@pytest.fixture
def teacher():
    test_teacher = Teacher(teacher_name='Test Teacher')
    save(test_teacher, conn)
    breakpoint()

    yield

    clear_table('teachers', conn)
    
def test_teacher(teacher):
    pass

