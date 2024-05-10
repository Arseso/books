import os
from socket import socket

connection = None

def init_socket() -> None:
    global connection
    connection = socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((os.getenv('host'), os.getenv('port')))


def close_connection() -> None:
    global connection
    connection.close()
