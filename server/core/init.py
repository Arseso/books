import socket
from server.core.logs import print_server_info
from server.config import SER_HOST, SER_PORTS_RANGE



def scan_ports() -> socket.socket:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in SER_PORTS_RANGE:
        try:
            serv.bind((SER_HOST, port))
            return serv
        except OSError:
            continue


def init_server() -> socket.socket:
    server = scan_ports()
    server.listen()
    print_server_info(server)
    return server

