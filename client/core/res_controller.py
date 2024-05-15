import re
from client.config import set_token_value
from client.ui.books_navigator.view import get_window
from client.requests.json_worker import get_books_from_json
from client.ui.dialogs import show_error_dialog


def response_controller(response: str) -> None:
    if re.findall(r"\[TOKEN](.*)\[END]", response):
        set_token_value(re.search(r"\[TOKEN](.*)\[END]", response).group(1))

    if re.findall(r"\[GET](.*)\[END]", response):
        books = get_books_from_json(re.search(r"\[GET](.*)\[END]", response).group(1))
        get_window().controller.books_to_table(books=books)

    if re.findall(r"\[EDIT](.*)\[END]", response):
        if re.search(r"\[EDIT](.*)\[END]", response).group(1) == "User not found.":
            pass  # Error dialog
        elif re.search(r"\[EDIT](.*)\[END]", response).group(1) == "You don't have permissions.":
            pass  # Error dialog
        elif re.search(r"\[EDIT](.*)\[END]", response).group(1) == "No book found.":
            pass  # Error dialog
        else:
            pass

    if re.findall(r"\[DEL](.*)\[END]", response):
        if re.search(r"\[DEL](.*)\[END]", response).group(1) == "User not found.":
            pass
        elif re.search(r"\[DEL](.*)\[END]", response).group(1) == "You don't have permissions.":
            pass  # Error dialog
        elif re.search(r"\[DEL](.*)\[END]", response).group(1) == "No book found.":
            pass  # Error dialog
        else:
            pass  # DEL book from UI

    if re.findall(r"\[UPD](.*)\[END]", response):
        if re.search(r"\[UPD](.*)\[END]", response).group(1) == "User not found.":
            pass
        elif re.search(r"\[UPD](.*)\[END]", response).group(1) != "[]":
            show_error_dialog("No updates found.")
