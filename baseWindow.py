from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton
from db_handler import DB_handler

class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QGridLayout()
        self.setLayout(layout)
        #интерфейс
        
        #логика
        
        