from PyQt6.QtWidgets import QApplication, QWidget, \
    QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QComboBox
from db_handler import DB_handler


class ZakazWindow(QWidget):
    """
        Класс окна для работы с заказами
    """
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        zakaz_lst = QListWidget()
        zakaz_lst.activated.connect(self.edit_zakaz)
        add_zakaz_btn = QPushButton("Добавить заказ")
        add_zakaz_btn.clicked.connect(self.add_zakaz)

        layout.addWidget(zakaz_lst, 0, 0)
        layout.addWidget(add_zakaz_btn, 1, 0)

    def edit_zakaz(self):
        """
        метод для редактирования заказа
        """
        pass

    def add_zakaz(self):
        """
        метод для добавления заказа
        """
        pass



