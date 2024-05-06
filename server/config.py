import os
from dotenv import load_dotenv

load_dotenv()

# SERVER
SER_HOST = os.getenv('SER_HOST')

SER_PORTS_RANGE = range(2000, 5000)

# POSTGRES
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")
DB_AUTOCOMMIT = True