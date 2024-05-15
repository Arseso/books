import sys

from PySide6.QtWidgets import QApplication
from client.config import get_token_value
from client.core.event_loop import init_event_loop, close_event_loop
from client.ui.auth import LoginWindow
from client.ui.books_navigator.view import init_books_navigator


def main():
    app = QApplication(sys.argv)
    init_event_loop()

    auth_window = LoginWindow()
    auth_window.show()

    app.exec()

    if get_token_value():
        books = init_books_navigator()
        books.show()
        app.exec()
    else:
        close_event_loop()
        sys.exit(0)

    close_event_loop()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
