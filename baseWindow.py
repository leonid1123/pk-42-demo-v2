from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton, QListWidget


class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Список товаров')
        layout = QGridLayout()
        self.setLayout(layout)
        self.role_label = QLabel("роль тут")
        layout.addWidget(self.role_label)
        self.goods_lst = QListWidget()
        layout.addWidget(self.goods_lst)