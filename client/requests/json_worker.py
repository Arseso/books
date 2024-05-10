from dataclasses import dataclass
from datetime import datetime

import jsons


@dataclass
class Book:
    creator_id: int
    permission: str
    author: str
    book_name: str
    src: str
    image_src: str
    price: float
    pages: int
    id: int = None
    last_updated: datetime = None


def get_json_from_book(book: Book | list[Book]) -> str:
    book_dict = jsons.dump(book)
    return jsons.dumps(book_dict, indent=4)


def get_book_from_json(json_data: str) -> Book | list[Book]:
    dict_data = jsons.loads(json_data)
    book = Book(**dict_data)
    return book
