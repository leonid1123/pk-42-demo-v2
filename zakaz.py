from PyQt6.QtWidgets import QApplication, QWidget, \
    QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QComboBox
from db_handler import DB_handler
from edit_zakaz import EditZakazWin


class ZakazWindow(QWidget):
    """
        Класс окна для работы с заказами
    """
    def __init__(self) -> None:
        super().__init__()
        self.my_db = DB_handler()
        layout = QGridLayout()
        self.setLayout(layout)
        self.zakaz_lst = QListWidget()
        self.zakaz_lst.activated.connect(self.edit_zakaz)
        add_zakaz_btn = QPushButton("Добавить заказ")
        add_zakaz_btn.clicked.connect(self.add_zakaz)

        layout.addWidget(self.zakaz_lst, 0, 0)
        layout.addWidget(add_zakaz_btn, 1, 0)
        self.get_all_zakaz()

    def edit_zakaz(self) -> None:
        """
        метод для редактирования заказа
        """
        self.edit_zakaz = EditZakazWin("Редактировать")
        self.edit_zakaz.show()

    def add_zakaz(self) -> None:
        """
        метод для добавления заказа
        """
        self.edit_zakaz = EditZakazWin("Добавить")
        self.edit_zakaz.show()

    def get_all_zakaz(self):
        sql = '''SELECT zakaz.`Артикул заказа`, zakaz.`Статус заказа`,
            pvz.`Адрес`, zakaz.`Дата заказа`,
            zakaz.`Дата доставки` 
            FROM `zakaz`
            INNER JOIN pvz
            ON zakaz.`Адрес пункта выдачи` = pvz.id'''
        self.my_db.cur.execute(sql)
        self.my_db.conn.commit()
        ans = self.my_db.cur.fetchone()
        self.zakaz_lst.clear()
        while ans:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]}"
            self.zakaz_lst.addItem(txt)
            ans = self.my_db.cur.fetchone()

        
