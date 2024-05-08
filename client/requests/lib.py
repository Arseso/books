import os

r_get_token = "{}:{}/token"
r_get_books = f"{os.getenv('token')}/book/get"
r_add_book = "{}/book/book/{}"
r_del_book_by_id = "{}/book/del/{}"
r_edit_book = "{}/book/edit/{}"
r_upd_books = "{}/book/upd/{}"


