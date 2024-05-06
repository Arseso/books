import asyncio
import socket


# Server
def print_server_info(server: socket.socket) -> None:
    print("[I] Server IP: {}, Server port: {}".format(*server.getsockname()))


def print_connected_client(address: str) -> None:
    print("[I] Client connected: {}".format(address))


def print_disconnected_client(client: socket.socket) -> None:
    print("[I] Client disconnected: {}".format(client.getpeername()))


def print_got_request(client: socket.socket) -> None:
    print("[I] Client: {}. Received request.".format(client.getpeername()))


def print_send_response(client: socket.socket) -> None:
    print("[I] Client: {}. Sent response.".format(client.getpeername()))


def print_server_closed_by_interrupt() -> None:
    print("[I] Server closed by keyboard interrupt.")


def print_server_closed_by_stop_iteration() -> None:
    print("[E] Server closed by someone's generator stop iteration.")


def print_server_new_user_registered(nickname: str) -> None:
    print(f"[I] New user (nickname: {nickname}) registered.")


def print_server_changed_role_for_user(object_token: str, subject_token: str) -> None:
    print(f"[I] User ({object_token}) set ADM role for: {subject_token}.")


def print_server_delete_user(object_token: str, subject_token: str) -> None:
    print(f"[I] User ({object_token}) deleted user {subject_token}.")


# Database
def print_database_created_connection(db_name: str, host: str, port: str) -> None:
    print("[I] Connection to database {} created at {}:{}".format(db_name, host, port))


def print_database_closed_connection(db_name) -> None:
    print("[I] Connection and cursor to database {} closed.".format(db_name))


def print_database_get_request_completed() -> None:
    print("[I] Request type GET to database was successfully completed.")


def print_database_set_request_completed() -> None:
    print("[I] Request type SET to database was successfully completed.")
