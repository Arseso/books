import os
import time
from threading import Thread
from client.core.connection import *
from client.requests.json_worker import get_book_from_json
from client.requests.req import get_updates

requests_queue = []


def response_controller(req_type: str, response: str) -> None:
    if req_type == 'AUTH':
        os.environ["token"] = response

    if req_type == 'GET':
        books = get_book_from_json(response)
        pass  # set books to UI

    if req_type == 'EDIT':
        if response == "User not found.":
            pass  # Error dialog
        if response == "You don't have permissions.":
            pass  # Error dialog
        if response == "No book found.":
            pass  # Error dialog

    if req_type == 'DEL':
        if response == "User not found.":
            pass  # Error dialog
        if response == "You don't have permissions.":
            pass  # Error dialog
        if response == "No book found.":
            pass  # Error dialog
        pass  # DEL book from UI
    if req_type == 'UPD':
        if response == "User not found.":
            pass  # Error dialog
        pass  # set updates to UI


def send_request(req_type: str, req_str: str) -> None:
    response = connection.send(req_str)
    response_controller(req_type, response.decode('utf-8'))


def event_loop() -> None:
    global requests_queue

    try:
        while True:
            while requests_queue:
                req_type, req_str = requests_queue.pop(0)
                action = Thread(target=send_request, args=(req_type, req_str))
                action.start()

            req_type, req_str = get_updates()
            action = Thread(target=send_request, args=(req_type, req_str))
            action.start()

    except KeyboardInterrupt:
        close_connection()


def init_event_loop():
    init_socket()
    loop = Thread(target=event_loop)
    loop.start()
