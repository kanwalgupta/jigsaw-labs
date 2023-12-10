import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DATABASE")
USER = os.getenv("user")
PASSWORD = os.getenv("password")