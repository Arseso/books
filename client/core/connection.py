import os
import socket
import client.config as cfg

def init_socket() -> socket.socket:
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((cfg.HOST, int(cfg.PORT)))
    connection.settimeout(3.0)
    return connection

