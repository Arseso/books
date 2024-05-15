import os
from builtins import str
from dataclasses import dataclass
from datetime import datetime
import jsons

import client.requests.lib as lib
from client.config import get_token_value
from client.requests.json_worker import Book, get_json_from_book

last_update = None


def get_token(login: str, password: str) -> str:
    return lib.r_get_token.format(login, password)


def get_books() -> str:
    global last_update
    last_update = datetime.now()
    return lib.r_get_books.format(get_token_value())


def delete_book(book: Book) -> str:
    return lib.r_del_book_by_id.format(get_token_value(), book.id)


def update_book(book: Book) -> str:
    json = get_json_from_book(book)
    return lib.r_edit_book.format(get_token_value(), json)


def get_updates() -> str:
    global last_update
    if last_update is None:
        last_update = datetime.now()
    temp = last_update
    last_update = datetime.now()
    return lib.r_upd_books.format(get_token_value(), temp.strftime("%Y-%m-%d %H:%M:%S.%f"))
