from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QApplication, QWidget, \
    QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QComboBox

from db_handler import DB_handler

class EditZakazWin(QWidget):
    def __init__(self, role):
        super().__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.artikul = QLineEdit()
        self.adress = QLineEdit()
        self.data_zakaza = QLineEdit()
        self.data_vidachi = QLineEdit()
        self.status = QComboBox()
        self.status.addItems(["завершён","новый"])
        layout.addRow("Артикул", self.artikul)
        layout.addRow("Адрес", self.adress)
        layout.addRow("Дата заказа", self.data_zakaza)
        layout.addRow("Дата выдачи", self.data_vidachi)
        layout.addRow("Статус",self.status)
        self.edit_zakaz = QPushButton(str(role))
        layout.addRow(self.edit_zakaz)


