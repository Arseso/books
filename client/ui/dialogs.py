import sys
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class AddEditDialog(QDialog):
    def __init__(self, parent=None, book=None):
        super().__init__(parent)
        self.book = book

        layout = QVBoxLayout()

        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Title")
        self.author_edit = QLineEdit()
        self.author_edit.setPlaceholderText("Author")
        self.pages_edit = QLineEdit()
        self.pages_edit.setPlaceholderText("Pages")
        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText("Price")

        if self.book:
            self.title_edit.setText(self.book.title)
            self.author_edit.setText(self.book.author)
            self.pages_edit.setText(str(self.book.pages))
            self.price_edit.setText(str(self.book.price))

        layout.addWidget(QLabel("Title:"))
        layout.addWidget(self.title_edit)
        layout.addWidget(QLabel("Author:"))
        layout.addWidget(self.author_edit)
        layout.addWidget(QLabel("Pages:"))
        layout.addWidget(self.pages_edit)
        layout.addWidget(QLabel("Price:"))
        layout.addWidget(self.price_edit)

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(buttons)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)
        self.setLayout(layout)

    def get_book_data(self):
        title = self.title_edit.text()
        author = self.author_edit.text()
        pages = int(self.pages_edit.text())
        price = float(self.price_edit.text())
        return title, author, pages, price


class ErrorDialog(QDialog):
    def __init__(self, error_message):
        super().__init__()

        self.setWindowTitle("Ошибка")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        label = QLabel(error_message)
        layout.addWidget(label)

        ok_button = QPushButton("ОК")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        self.setLayout(layout)


def show_error_dialog(error_message: str) -> None:
    dialog = ErrorDialog(error_message)
    dialog.show()
