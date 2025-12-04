from PyQt6.QtWidgets import QApplication, QWidget, \
    QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QComboBox
from db_handler import DB_handler
from editWindow import EditWindow


class BaseWindow(QWidget):
    def __init__(self, _role, _fio, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = _role
        self.FIO = _fio
        self.setWindowTitle(f"Товары. {self.FIO}, {self.role}")
        self.myDB = DB_handler()
        layout = QGridLayout()
        self.setLayout(layout)
        # интерфейс
        self.main_lst = QListWidget()
        self.main_lst.itemDoubleClicked.connect(self.open_edit_window)
        self.filter = QComboBox()#фильтр по поставщику
        self.filter.activated.connect(self.get_filter)
        self.up_btn = QPushButton("По возрастанию")  # сортировка по количеству на складе
        self.up_btn.clicked.connect(self.sort_up)
        self.down_btn = QPushButton("По убыванию")  # сортировка по количеству на складе
        self.down_btn.clicked.connect(self.sort_down)
        self.txt_search = QLineEdit()  # поиск по текстовым полям
        if self.role in ['Менеджер', 'Администратор']:
            self.txt_search.textChanged.connect(self.search_slot)
        else:
            self.txt_search.setPlaceholderText('нет!')
        layout.addWidget(self.main_lst, 1, 0, 1, 3)
        layout.addWidget(self.filter, 0, 0)
        layout.addWidget(self.up_btn, 0, 1)
        layout.addWidget(self.down_btn, 0, 2)
        layout.addWidget(self.txt_search, 2, 0)
        self.get_all_and_print()
        self.set_filter()

        #  логика
    def get_all_and_print(self):
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar'
        self.myDB.cur.execute(sql)
        ans = self.myDB.cur.fetchone()
        while ans is not None:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]} "
            self.main_lst.addItem(txt)
            ans = self.myDB.cur.fetchone()

    def sort_up(self):
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar ORDER BY `Кол-во на складе` ASC'
        self.myDB.cur.execute(sql)
        ans = self.myDB.cur.fetchone()
        while ans is not None:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]} "
            self.main_lst.addItem(txt)
            ans = self.myDB.cur.fetchone()

    def sort_down(self):
        self.main_lst.clear()
        sql = 'SELECT * FROM tovar  ORDER BY `Кол-во на складе` DESC'
        self.myDB.cur.execute(sql)
        ans = self.myDB.cur.fetchone()
        while ans is not None:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]} "
            self.main_lst.addItem(txt)
            ans = self.myDB.cur.fetchone()

    def set_filter(self):
        self.filter.addItem("Все поставщики")
        sql = 'SELECT DISTINCT `Поставщик` FROM tovar'
        self.myDB.cur.execute(sql)
        ans = self.myDB.cur.fetchone()
        while ans is not None:
            self.filter.addItem(f"{ans[0]}")
            ans = self.myDB.cur.fetchone()

    def get_filter(self):
        postav = self.filter.currentText()
        if postav != "Все поставщики":
            self.main_lst.clear()
            sql = 'SELECT * FROM tovar WHERE `Поставщик`=%s'
            self.myDB.cur.execute(sql, (postav,))
            ans = self.myDB.cur.fetchone()
            while ans is not None:
                txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]} "
                self.main_lst.addItem(txt)
                ans = self.myDB.cur.fetchone()
        else:
            self.get_all_and_print()

    def search_slot(self):
        user_input = '%' + self.txt_search.text() + '%'
        sql = "SELECT * FROM tovar WHERE `Наименование товара` LIKE %s OR `Поставщик` LIKE %s"
        self.myDB.cur.execute(sql, (user_input, user_input))
        ans = self.myDB.cur.fetchone()
        self.main_lst.clear()
        while ans is not None:
            txt = f"{ans[0]};{ans[1]};{ans[2]};{ans[3]};{ans[4]};{ans[5]};{ans[6]};{ans[7]};{ans[8]};{ans[9]} "
            self.main_lst.addItem(txt)
            ans = self.myDB.cur.fetchone()

    def open_edit_window(self):
        item_text = self.main_lst.selectedItems()
        line = item_text[0].text()
        selected_item_to_edit = line.split(";")
        self.edit_win = EditWindow(selected_item_to_edit)
        self.edit_win.show()
