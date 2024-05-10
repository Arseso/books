import os
from builtins import str
from dataclasses import dataclass
from datetime import datetime
import jsons

import client.requests.lib as lib
from client.requests.json_worker import Book, get_json_from_book

last_update = None


def get_token(login: str, password: str) -> tuple[str, str]:
    return "AUTH", lib.r_get_token.format(login, password)


def get_books() -> tuple[str, str]:
    global last_update
    last_update = datetime.now()
    return "GET", lib.r_get_books.format(os.getenv('token'))


def delete_book(book: Book) -> tuple[str, str]:
    return "DEL", lib.r_del_book_by_id.format(os.getenv('token'), book.id)


def update_book(book: Book) -> tuple[str, str]:
    json = get_json_from_book(book)
    return "EDIT", lib.r_edit_book.format(os.getenv('token'), json)


def get_updates() -> tuple[str, str]:
    global last_update
    temp = last_update
    last_update = datetime.now()
    return "UPD", lib.r_upd_books.format(os.getenv('token'), temp.strftime("%Y-%m-%d %H:%M:%S.%f"))
