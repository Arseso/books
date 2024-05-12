import os
import sys
from PySide6.QtWidgets import QApplication

import client.requests.req
from client.config import get_token_value
from client.core.event_loop import init_event_loop, close_event_loop
from client.ui.auth import init_auth
from client.ui.books_navigator import init_books_navigator


def main():
    init_event_loop()
    app = QApplication(sys.argv)
    init_auth(app)
    if get_token_value():
        print("inited")
        init_books_navigator(app)
    else:
        close_event_loop()
        sys.exit(0)
    close_event_loop()


if __name__ == '__main__':
    main()
