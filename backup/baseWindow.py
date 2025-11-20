from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton, QListWidget, QComboBox
from db_handler import Db_handler


class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Список товаров')
        self.setGeometry(0,0,1200,700)
        layout = QGridLayout()
        self.setLayout(layout)
        self.search_entry = QLineEdit()
        self.search_entry.textEdited.connect(self.get_search)
        layout.addWidget(self.search_entry,0,0)
        self.filter = QComboBox()
        self.filter.activated.connect(self.set_filter)
        layout.addWidget(self.filter,0,1)
        self.sort_up_btn = QPushButton("UP")
        self.sort_up_btn.clicked.connect(self.sort_up)
        layout.addWidget(self.sort_up_btn,0,2)
        self.sort_down_btn = QPushButton("DOWN")
        self.sort_down_btn.clicked.connect(self.sort_down)
        layout.addWidget(self.sort_down_btn,0,3)
        self.role_label = QLabel("роль тут")
        layout.addWidget(self.role_label,0,4)
        self.goods_lst = QListWidget()
        layout.addWidget(self.goods_lst,1,0,1,4)
        exit_btn = QPushButton("выход")
        exit_btn.clicked.connect(self.close_window)
        layout.addWidget(exit_btn,2,0)
        self.db = Db_handler()
        self.populate_filter()
        self.get_all_goods()

    def get_all_goods(self):
        self.db.cur.execute('SELECT * FROM tovar')
        ans = self.db.cur.fetchone()
        self.goods_lst.clear()
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item + ', ')
            self.goods_lst.addItem(tmp_str)
            ans = self.db.cur.fetchone()

    def close_window(self):
        self.close()

    def sort_up(self):
        sql = 'SELECT * FROM tovar ORDER BY Кол_во_на_складе DESC'
        self.db.cur.execute(sql)
        ans = self.db.cur.fetchone()
        self.goods_lst.clear()
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item + ', ')
            self.goods_lst.addItem(tmp_str)
            ans = self.db.cur.fetchone()


    def sort_down(self):
        sql = 'SELECT * FROM tovar ORDER BY Кол_во_на_складе ASC'
        self.db.cur.execute(sql)
        ans = self.db.cur.fetchone()
        self.goods_lst.clear()
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item + ', ')
            self.goods_lst.addItem(tmp_str)
            ans = self.db.cur.fetchone()

    def set_filter(self):
        input = self.filter.currentText()
        sql = 'SELECT * FROM tovar WHERE Поставщик = ?'
        if input != "Все поставщики":
            self.db.cur.execute(sql,(input,))
            ans = self.db.cur.fetchone()
            self.goods_lst.clear()
            while ans is not None:
                tmp_str=''
                for item in ans:
                    tmp_str += (item + ', ')
                self.goods_lst.addItem(tmp_str)
                ans = self.db.cur.fetchone()
        else:
            self.get_all_goods()


    def populate_filter(self):
        sql = 'SELECT DISTINCT Поставщик FROM tovar '
        self.db.cur.execute(sql)
        ans = self.db.cur.fetchall()
        self.filter.clear()
        self.filter.addItem("Все поставщики")
        for item in ans:
            self.filter.addItem(item[0])

    def get_search(self, text):
        new_text = f"%{text}%"
        sql = 'SELECT * FROM tovar WHERE Производитель LIKE ? OR Артикул LIKE ?'
        self.db.cur.execute(sql,(new_text,new_text))
        ans = self.db.cur.fetchone()
        self.goods_lst.clear()
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item + ', ')
            self.goods_lst.addItem(tmp_str)
            ans = self.db.cur.fetchone()

