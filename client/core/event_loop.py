import time
from threading import Thread

from client.core.connection import *
from client.core.req_queue import is_queue_not_empty, pop_from_queue
from client.requests.req import get_updates

from client.core.res_controller import response_controller

_connection = None
_close = False


def send_request(req_str: str) -> None:
    try:
        global _connection
        print(req_str)
        _connection.sendall(req_str.encode())
        response = _connection.recv(8192)
        response_controller(response.decode('utf-8')[:-1])
    except TimeoutError:
        print("Request timed out.")


def event_loop() -> None:
    global _close
    while not _close:
        while is_queue_not_empty():
            req_str = pop_from_queue()
            action = Thread(target=send_request, args=(req_str,))
            action.start()

        time.sleep(1)
        req_type, req_str = get_updates()
        action = Thread(target=send_request, args=(req_str,))
        action.start()


def init_event_loop():
    global _connection
    try:
        _connection = init_socket()
        loop = Thread(target=event_loop)
        loop.start()
    except KeyboardInterrupt:
        _connection.close()


def close_event_loop():
    global _close
    _close = True
