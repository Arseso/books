import sys
from PySide6.QtWidgets import QApplication

from client.config import get_token_value
from client.core.event_loop import init_event_loop, close_event_loop
from client.ui.auth import LoginWindow
from client.ui.books_navigator.view import init_books_navigator


def main():
    print("qq")
    app = QApplication(sys.argv)  # Create QApplication instance first
    print("qq")
    init_event_loop()
    print("qq")

    auth_window = LoginWindow()  # Create LoginWindow instance after QApplication
    auth_window.show()  # Show the authentication window

    app.exec()  # Start the application event loop

    if get_token_value():
        books = init_books_navigator()
        books.show()  # Show the books navigator window
        app.exec()  # Start the application event loop for books navigator
    else:
        close_event_loop()
        sys.exit(0)

    close_event_loop()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

