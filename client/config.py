import os
from dotenv import load_dotenv

load_dotenv()

# SERVER
HOST = os.getenv('SER_HOST')
PORT = os.getenv('SER_PORT')

_TOKEN = None


def get_token_value() -> str:
    global _TOKEN
    return _TOKEN


def set_token_value(token: str) -> None:
    global _TOKEN
    _TOKEN = token
