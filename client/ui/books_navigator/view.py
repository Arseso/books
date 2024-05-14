from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from client.ui.books_navigator.controller import BookStoreController


class BookStoreView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Store")
        self.resize(600, 400)

        self.setup_table()

        self.controller = BookStoreController(self)

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Title", "Author", "Pages", "Price"])
        self.setCentralWidget(self.table)

    def add_book_to_table(self, title, author, pages, price):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(title))
        self.table.setItem(row_position, 1, QTableWidgetItem(author))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(pages)))
        self.table.setItem(row_position, 3, QTableWidgetItem(str(price)))

    def update_table(self):
        self.table.setRowCount(0)
        for book in self.controller.model:
            self.add_book_to_table(book.title, book.author, book.pages, book.price)


_window = BookStoreView()


def get_window() -> BookStoreView:
    return _window


def init_books_navigator() -> BookStoreView:
    return _window
