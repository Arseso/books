import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QWidget, QFileDialog, QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout, QDialogButtonBox, QComboBox
from PySide6.QtGui import QAction


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


class BookStore(QMainWindow):
    def __init__(self):
        super().__init__()

        self.books = []

        self.setWindowTitle("Book Store")
        self.resize(600, 400)

        self.setup_menu()
        self.setup_table()

    def setup_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        load_action = QAction("Load from File", self)
        load_action.triggered.connect(self.load_from_file)
        file_menu.addAction(load_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = menu_bar.addMenu("Edit")

        add_action = QAction("Add Book", self)
        add_action.triggered.connect(self.add_book)
        edit_menu.addAction(add_action)

        edit_action = QAction("Edit Book", self)
        edit_action.triggered.connect(self.edit_book)
        edit_menu.addAction(edit_action)

        delete_action = QAction("Delete Book", self)
        delete_action.triggered.connect(self.delete_book)
        edit_menu.addAction(delete_action)

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Title", "Author", "Pages", "Price"])
        self.setCentralWidget(self.table)

    def load_from_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split()
                    if len(data) == 4:
                        title, author, pages, price = data
                        self.books.append((title, author, int(pages), float(price)))
                        self.add_book_to_table(title, author, int(pages), float(price))

    def add_book(self):
        dialog = AddEditDialog(self)
        if dialog.exec_():
            title, author, pages, price = dialog.get_book_data()
            self.books.append((title, author, pages, price))
            self.add_book_to_table(title, author, pages, price)

    def edit_book(self):
        row = self.table.currentRow()
        if row >= 0:
            current_book = self.books[row]
            dialog = AddEditDialog(self, book=current_book)
            if dialog.exec_():
                title, author, pages, price = dialog.get_book_data()
                self.books[row] = (title, author, pages, price)
                self.update_table()

    def delete_book(self):
        row = self.table.currentRow()
        if row >= 0:
            del self.books[row]
            self.table.removeRow(row)

    def add_book_to_table(self, title, author, pages, price):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(title))
        self.table.setItem(row_position, 1, QTableWidgetItem(author))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(pages)))
        self.table.setItem(row_position, 3, QTableWidgetItem(str(price)))

    def update_table(self):
        self.table.setRowCount(0)
        for book in self.books:
            self.add_book_to_table(*book)


def init_books_navigator(app: QApplication) -> None:
    window = BookStore()
    window.show()
    app.exec()

