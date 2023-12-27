import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("database")
TEST_DATABASE = os.getenv("test_database")