import server.api.api_usr as usr
import server.api.api_books as books

lib = {
    # USER requests
    r"(\w+):(\w+)\/token": usr.get_token,
    r"(\w+)\/adm\/set\/(\w+)": usr.set_admin,
    r"(\w+)\/usr\/del\/(\w+)": usr.del_user,

    # BOOKS requests
    r"(\w+)\/book\/get":  books.get_books,
    r"(\w+)\/book\/add\/(\w+)": books.add_book,
    r"(\w+)\/book\/del\/(\d+)": books.del_book,
    r"(\w+)\/book\/edit\/(\w+)": books.set_book,
    r"(\w+)\/book\/upd\/(\w+)": books.get_books_update


}