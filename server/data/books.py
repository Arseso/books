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

    def get_params(self):
        return self.creator_id, self.permission, self.author, self.book_name, self.src, self.image_src, self.price, self.pages


def get_book_from_json(json_data: str) -> Book:
    dict_data = jsons.loads(json_data)
    book = Book(**dict_data)
    return book


def get_json_from_book(book: Book | list[Book]) -> str:
    book_dict = jsons.dump(book)
    return jsons.dumps(book_dict, indent=4)


expected_book = Book(1, "public", "1", "qq", "str", "str", .0, 100)

assert get_book_from_json(
    get_json_from_book(expected_book)) == expected_book
