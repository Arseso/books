from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction
from client.ui.dialogs import AddEditDialog
from client.requests.json_worker import Book

from client.core.req_queue import append_to_queue
from client.requests.req import get_books, update_book, delete_book


def load_from_server() -> None:
    append_to_queue(get_books())


class BookStoreController:
    def __init__(self, view):
        self.view = view
        self.model = []

        self.setup_menu()

    def setup_menu(self):
        file_menu = self.view.menuBar().addMenu("File")

        load_action = QAction("Load from Server", self.view)
        load_action.triggered.connect(load_from_server)
        file_menu.addAction(load_action)

        exit_action = QAction("Exit", self.view)
        exit_action.triggered.connect(self.view.close)
        file_menu.addAction(exit_action)

        edit_menu = self.view.menuBar().addMenu("Edit")

        add_action = QAction("Add Book", self.view)
        add_action.triggered.connect(self.add_book)
        edit_menu.addAction(add_action)

        edit_action = QAction("Edit Book", self.view)
        edit_action.triggered.connect(self.edit_book)
        edit_menu.addAction(edit_action)

        delete_action = QAction("Delete Book", self.view)
        delete_action.triggered.connect(self.delete_book)
        edit_menu.addAction(delete_action)

    def books_to_table(self, books: list[Book]) -> None:
        for book in books:
            self.model.append(book)
            self.view.add_book_to_table(book.book_name, book.author, book.pages, book.price)

    def add_book(self):
        dialog = AddEditDialog(self.view)
        if dialog.exec_():
            title, author, pages, price = dialog.get_book_data()
            book = Book(title, author, pages, price)
            self.model.append(book)
            self.view.add_book_to_table(title, author, pages, price)

    def edit_book(self):
        row = self.view.table.currentRow()
        if row >= 0:
            current_book = self.model[row]
            dialog = AddEditDialog(self.view, book=current_book)
            if dialog.exec_():
                title, author, pages, price = dialog.get_book_data()
                self.model[row] = Book(title, author, pages, price)
                self.view.update_table()

    def delete_book(self):
        row = self.view.table.currentRow()
        if row >= 0:
            del self.model[row]
            self.view.table.removeRow(row)
