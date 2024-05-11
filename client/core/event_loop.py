import re
import time
from threading import Thread

from client.core.connection import *
from client.requests.json_worker import get_book_from_json
from client.requests.req import get_updates
from client.config import set_token_value
from client.ui.dialogs import show_error_dialog

requests_queue = []
connection = None

_books_received = False


def append_to_queue(request: str) -> None:
    global requests_queue
    requests_queue.append(request)


def response_controller(response: str) -> None:
    global _books_received
    print(response)
    if re.match(r"\[TOKEN](.*)$", response):
        set_token_value(re.search(r"\[TOKEN](.*)$", response).group(1))
        print(re.search(r"\[TOKEN](.*)$", response).group(1))

    if re.match(r"\[GET](.*)$", response):
        books = get_book_from_json(re.search(r"[GET](.*)$", response).group(1))
        _books_received = True

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


def send_request(req_str: str) -> None:
    try:
        global connection
        print(req_str)
        connection.sendall(req_str.encode())
        response = connection.recv(8192)
        response_controller(response.decode('utf-8')[:-1])
    except TimeoutError:
        print("Request timed out.")


def event_loop() -> None:
    global requests_queue
    while True:
        while requests_queue:
            req_str = requests_queue.pop(0)
            action = Thread(target=send_request, args=(req_str,))
            action.start()

        if _books_received:
            time.sleep(1)
            req_type, req_str = get_updates()

            action = Thread(target=send_request, args=(req_str,))
            action.start()


def init_event_loop():
    global connection
    try:
        connection = init_socket()
        loop = Thread(target=event_loop)
        loop.start()
    except KeyboardInterrupt:
        connection.close()
