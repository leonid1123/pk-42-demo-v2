import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Авторизация')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())