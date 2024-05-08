import os

r_get_token = "{}:{}/get/token"
r_get_books = f"{os.getenv('token')}/get/books"
r_add_book = "{}/add/book/{}"
r_del_book_by_id = "{}/del/book/{}"
r_edit_book = "{}/set/book/{}"
r_get_updates = "{}/get/book/update"

# BOOKS requests
r"(\w+)\/get\/books":  books.get_books,
r"(\w+)\/add\/book\/(\w+)": books.add_book,
r"(\w+)\/del\/book\/(\d+)": books.del_book,
r"(\w+)\/set\/book\/(\w+)": books.set_book,
r"(\w+)\/get\/books\/update\/(\w+)": books.get_books_update