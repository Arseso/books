import re
from client.config import set_token_value
from client.ui.books_navigator.view import get_window
from client.requests.json_worker import get_book_from_json
from client.ui.dialogs import show_error_dialog


def response_controller(response: str) -> None:
    if re.match(r"\[TOKEN](.*)$", response):
        set_token_value(re.search(r"\[TOKEN](.*)$", response).group(1))

    if re.match(r"\[GET](.*)$", response):
        books = get_book_from_json(re.search(r"[GET](.*)$", response).group(1))
        get_window().controller.books_to_table(books=books)

    if re.match(r"\[EDIT](.*)$", response):
        if re.search(r"\[EDIT](.*)$", response).group(1) == "User not found.":
            pass  # Error dialog
        elif re.search(r"\[EDIT](.*)$", response).group(1) == "You don't have permissions.":
            pass  # Error dialog
        elif re.search(r"\[EDIT](.*)$", response).group(1) == "No book found.":
            pass  # Error dialog
        else:
            pass

    if re.match(r"\[DEL](.*)$", response):
        if re.search(r"\[DEL](.*)$", response).group(1) == "User not found.":
            pass
        elif re.search(r"\[DEL](.*)$", response).group(1) == "You don't have permissions.":
            pass  # Error dialog
        elif re.search(r"\[DEL](.*)$", response).group(1) == "No book found.":
            pass  # Error dialog
        else:
            pass  # DEL book from UI

    if re.match(r"\[UPD](.*)$", response):
        if re.search(r"\[UPD](.*)$", response).group(1) == "User not found.":
            pass
        elif re.search(r"\[UPD](.*)$", response).group(1) != "[]":
            show_error_dialog("No updates found.")
