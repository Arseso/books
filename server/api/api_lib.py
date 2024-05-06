import server.api.api_usr as usr
import server.api.api_books as books

lib = {
    # USER requests
    r"(\w+):(\w+)\/get\/token": usr.get_token,
    r"(\w+)\/set\/admin\/(\w+)": usr.set_admin,
    r"(\w+)\/del\/user\/(\w+)": usr.del_user,

    # BOOKS requests
    r"(\w+)\/get\/books":  books.get_books,
    r"(\w+)\/add\/book\/(\w+)": books.add_book,
    r"(\w+)\/del\/book\/(\d+)": books.del_book,
    r"(\w+)\/set\/book\/(\w+)": books.set_book,
    r"(\w+)\/get\/books\/update\/(\w+)": books.get_books_update


}