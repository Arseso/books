from select import select
from socket import socket
import server.core.logs as logs
from server.api.api_main import make_response
from server.core.init import init_server
from server.data.requests import con_cur_close

__tasks = []
__to_read = {}
__to_write = {}


def check_connection(server: socket) -> tuple[str, socket]:
    while True:
        yield "R", server

        client, address = server.accept()
        logs.print_connected_client(address)

        __tasks.append(handle_request(client))


def handle_request(client: socket) -> tuple[str, socket]:
    while True:
        yield "R", client

        request = client.recv(8192)
        logs.print_got_request(client)
        if not request:
            logs.print_disconnected_client(client)
            break
        else:
            yield "W", client

            response = make_response(request.decode())
            client.send(response.encode())
            logs.print_send_response(client)


def event_loop() -> None:
    global __to_read, __to_write, __tasks

    server = init_server()
    __tasks.append(check_connection(server))

    try:
        while any([__tasks, __to_read, __to_write]):

            while not __tasks:
                readable, writable, _ = select(__to_read, __to_write, [])

                for sock in readable:
                    __tasks.append(__to_read.pop(sock))
                for sock in writable:
                    __tasks.append(__to_write.pop(sock))

            task = __tasks.pop(0)
            try:
                mode, sock = next(task)
            except StopIteration:
                continue

            if mode == "R":
                __to_read[sock] = task
            if mode == "W":
                __to_write[sock] = task

    except KeyboardInterrupt:
        con_cur_close()
        server.close()
        logs.print_server_closed_by_interrupt()
