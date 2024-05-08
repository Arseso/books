from datetime import datetime

from server.api.api_usr import get_id_by_token

from server.data.requests import execute_get_request as db_get
from server.data.requests import execute_set_request as db_set
import server.data.requests_library as lib
from server.data.books import get_book_from_json, get_json_from_book, Book

from server.data.usr import is_admin


def get_books(usr_token: str) -> str:
    user = get_id_by_token(usr_token)
    if user == -1:
        return "User not found."
    else:
        if is_admin(usr_token):
            books = db_get(lib.GET_BOOKS_ADM)
        else:
            books = db_get(lib.GET_BOOKS_USER.format(user))
        data_books = []
        for book in books:
            data_books.append(Book(*book))
    return get_json_from_book(data_books)


def add_book(token: str, book_json: str) -> str | None:
    user = get_id_by_token(token)
    if user == -1:
        return "User not found."
    book = get_book_from_json(book_json)
    db_set(lib.ADD_BOOK.format(*book.get_params()))
    return None


def get_books_update(usr_token: str, last_update: str) -> str:
    user = get_id_by_token(usr_token)
    if user == -1:
        return "User not found."
    else:
        if is_admin(usr_token):
            books = db_get(lib.GET_BOOKS_UPDATE_ADM.format(last_update))
        else:
            books = db_get(lib.GET_BOOKS_UPDATE_USER.format(user, last_update))
        data_books = []
        for book in books:
            data_books.append(Book(*book))
    return get_json_from_book(data_books)


def del_book(token: str, book_id: int) -> str | None:
    user = get_id_by_token(token)
    if user == -1:
        return "User not found."
    creator = db_get(lib.GET_BOOK_CREATOR_ID.format(book_id))
    if len(creator) == 0:
        return "No book found."
    if is_admin(token) or user == creator[0][0]:
        db_set(lib.DEL_BOOK.format(book_id))
        return None
    else:
        return "You don't have permissions."


def set_book(token: str, book_json: str) -> str | None:
    user = get_id_by_token(token)
    if user == -1:
        return "User not found."
    book = get_book_from_json(book_json)
    creator = db_get(lib.GET_BOOK_CREATOR_ID.format(book.id))
    if len(creator) == 0:
        return "No book found."
    if is_admin(token) or user == creator[0][0]:
        db_set(lib.UPD_BOOK.format(*book.get_params(), book.id))
        return None
    else:
        return "You don't have permissions."


#print(add_book("gy0so", """{"id": 1, "creator_id": 4, "permission": "private", "author": "T", "book_name": "1",
#"src": "1", "image_src": "1", "price": 100, "pages": 500}"""))
#print(del_book("gy0so", 5))

#print(get_books_update("gy0so", "2024-05-09 00:34:11.224905"), sep="\n")