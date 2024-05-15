from dataclasses import dataclass
from datetime import datetime
from typing import List

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



def get_json_from_book(book: Book | list[Book]) -> str:
    book_dict = jsons.dump(book)
    return jsons.dumps(book_dict, indent=4)


def get_books_from_json(json_data):
    try:
        # Check if the json_data is a string
        if isinstance(json_data, str):
            # Attempt to load a list of Book objects
            books = jsons.loads(json_data, List[Book])
            return books
        else:
            # If json_data is not a string, assume it's already a list of Book objects
            return jsons.load(json_data, List[Book])
    except jsons.exceptions.DeserializationError as e:
        print(f"Deserialization error: {e}")
        return []