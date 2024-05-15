import sys

from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from client.core.req_queue import append_to_queue
from client.config import get_token_value
from client.requests.req import get_token


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_login = QLabel("Логин:")
        self.layout.addWidget(self.label_login)

        self.e_login = QLineEdit()
        self.layout.addWidget(self.e_login)

        self.label_password = QLabel("Пароль:")
        self.layout.addWidget(self.label_password)

        self.e_passwd = QLineEdit()
        self.e_passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.e_passwd)

        self.b_login = QPushButton("Войти")
        self.b_login.clicked.connect(self.login)
        self.layout.addWidget(self.b_login)

    def login(self):
        if len(self.e_login.text()) != 0 and len(self.e_passwd.text()) != 0:
            login = self.e_login.text()
            password = self.e_passwd.text()

            append_to_queue(get_token(login, password))

        while not get_token_value():
            pass
        print("Auth success: " + get_token_value())
        self.close()


def init_auth() -> LoginWindow:
    window = LoginWindow()
    print("inited3")
    return window
