import os
import queue
import time
from multiprocessing import Manager
from threading import Thread
from client.core.connection import *
from client.requests.json_worker import get_book_from_json
from client.requests.req import get_updates
from client.config import set_token_value

requests_queue = []
connection = None


def append_to_queue(item):
    global requests_queue
    requests_queue.append()


def response_controller(req_type: str, response: str) -> None:
    if req_type == 'AUTH':
        set_token_value(response)
        print("Authentication successful:" + response)

    if req_type == 'GET':
        books = get_book_from_json(response)
        pass  # set books to UI

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
            print("User not found.")
        if response != "[]":
            print(response)


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
            print("main request")
            action = Thread(target=send_request, args=(req_type, req_str))
            action.start()
        time.sleep(1)
        req_type, req_str = get_updates()
        print("update: " + req_str)

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


def get_token() -> str:
    global TOKEN
    return TOKEN
