import os
from dotenv import load_dotenv

load_dotenv()

# SERVER
host = os.getenv('SER_HOST')
port = os.getenv('SER_PORT')

TOKEN = None


def get_token_value() -> str:
    global TOKEN
    return TOKEN


def set_token_value(token: str) -> None:
    global TOKEN
    TOKEN = token
    print(TOKEN + "1")
