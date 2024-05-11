import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton


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
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    dialog = ErrorDialog(error_message)
    dialog.exec()
    app.exec()


