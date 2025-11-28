from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton, QListWidget, QComboBox
from db_handler import DB_handler


class BaseWindow(QWidget):
    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent, flags)