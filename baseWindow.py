from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton, QListWidget
from db_handler import Db_handler


class BaseWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Список товаров')
        self.setGeometry(0,0,1200,700)
        layout = QGridLayout()
        self.setLayout(layout)
        self.role_label = QLabel("роль тут")
        layout.addWidget(self.role_label,0,0)
        self.goods_lst = QListWidget()
        layout.addWidget(self.goods_lst,1,0)
        exit_btn = QPushButton("выход")
        exit_btn.clicked.connect(self.close_window)
        layout.addWidget(exit_btn,2,0)
        self.get_all_goods()

    def get_all_goods(self):
        db = Db_handler()
        db.cur.execute('SELECT * FROM tovar')
        ans = db.cur.fetchone()
        while ans is not None:
            tmp_str=''
            for item in ans:
                tmp_str += (item + ', ')
            self.goods_lst.addItem(tmp_str)
            ans = db.cur.fetchone()

    def close_window(self):
        self.close()

