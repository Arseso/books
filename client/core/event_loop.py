import os
import queue
import time
from multiprocessing import Manager
from threading import Thread
from client.core.connection import *
from client.requests.json_worker import get_book_from_json
from client.requests.req import get_updates
from client.config import set_token_value
from client.ui.dialogs import show_error_dialog


requests_queue = []
connection = None

_books_received = False

def append_to_queue(request: tuple[str, str]):
    global requests_queue
    requests_queue.append(request)


def response_controller(req_type: str, response: str) -> None:
    global _books_received
    if req_type == 'AUTH':
        set_token_value(response)

        show_error_dialog("you gay")

    if req_type == 'GET':
        books = get_book_from_json(response)
        _books_received = True

    if req_type == 'EDIT':
        if response == "User not found.":
            pass  # Error dialog
        elif response == "You don't have permissions.":
            pass  # Error dialog
        elif response == "No book found.":
            pass  # Error dialog
        else:
            pass

    if req_type == 'DEL':
        if response == "User not found.":
            pass
        elif response == "You don't have permissions.":
            pass  # Error dialog
        elif response == "No book found.":
            pass  # Error dialog
        else:
            pass  # DEL book from UI
    if req_type == 'UPD':
        if response == "User not found.":
            pass
        elif response != "[]":
            show_error_dialog("No updates found.")


def send_request(req_type: str, req_str: str) -> None:
    try:
        global connection
        connection.sendall(req_str.encode())
        response = connection.recv(8192)
        response_controller(req_type, response.decode('utf-8')[:-1])
    except TimeoutError:
        print("Request timed out.")


def event_loop() -> None:
    global requests_queue
    while True:
        while requests_queue:
            req_type, req_str = requests_queue.pop(0)
            action = Thread(target=send_request, args=(req_type, req_str))
            action.start()

        if _books_received:
            time.sleep(1)
            req_type, req_str = get_updates()

            action = Thread(target=send_request, args=(req_type, req_str))
            action.start()


def init_event_loop():
    global connection
    try:
        connection = init_socket()
        loop = Thread(target=event_loop)
        loop.start()
    except KeyboardInterrupt:
        connection.close()
