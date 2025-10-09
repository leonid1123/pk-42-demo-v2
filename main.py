#https://github.com/leonid1123/pk-42-demo-v2
#    Set-ExecutionPolicy RemoteSigned
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton
from db_handler import Db_handler
from baseWindow import BaseWindow
import hashlib


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Авторизация')
        main_widget = QWidget()
        self.layout = QGridLayout()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)
        self.setUI()
        self.show()
    
    def setUI(self):
        self.layout.addWidget(QLabel('Логин'), 0, 0)
        self.layout.addWidget(QLabel('Пароль'), 1, 0)
        self.login_entry = QLineEdit()
        self.pass_entry = QLineEdit()
        self.layout.addWidget(self.login_entry,0,1)
        self.layout.addWidget(self.pass_entry,1,1)
        self.login_btn = QPushButton("Вход")
        self.login_btn.clicked.connect(self.login_handler)
        self.guest_btn = QPushButton("Гость")
        self.guest_btn.clicked.connect(self.guest_handler)
        self.layout.addWidget(self.login_btn,3,0,1,2)
        self.layout.addWidget(self.guest_btn,4,0,1,2)

    def login_handler(self):
        login_input = self.login_entry.text().strip()
        pass_input = self.pass_entry.text().strip()
        db = Db_handler()
        sql='SELECT password,role FROM users WHERE login=?'
        db.cur.execute(sql,(login_input,))
        ans = db.cur.fetchone()
        if ans:
            m = hashlib.sha256()
            m.update(pass_input.encode())
            if m.hexdigest() == ans[0]:
                self.base_window = BaseWindow()
                self.base_window.role_label.setText(self.role_handler(ans[1]))
                self.base_window.show()

       
    def guest_handler(self):
        self.base_window = BaseWindow()
        self.base_window.role_label.setText('Гость')
        self.base_window.show()

    def role_handler(self, role_int):
        if role_int == 2:
            return "Авторизованный клиент"
        if role_int == 3:
            return "Менеджер"
        if role_int == 4:
            return "Администратор"




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())