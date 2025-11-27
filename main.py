import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget,\
    QMainWindow, QGridLayout, QLabel, QLineEdit,\
    QPushButton
from db_handler import DB_handler
from baseWindow import BaseWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = 'Guest'
        self.FIO = ''
        self.bw = None
        self.myDb = DB_handler()
        self.setWindowTitle('Обувь')
        
        layout = QGridLayout()
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_widget.setLayout(layout)
        
        layout.addWidget(QLabel("Логин"),0,0)
        layout.addWidget(QLabel("Пароль"),1,0)
        
        self.login_entry = QLineEdit()
        self.pass_entry = QLineEdit()
        self.login_btn = QPushButton("Вход")
        self.login_btn.clicked.connect(self.password_login)
        self.guest_btn = QPushButton("Гостевой вход")
        self.guest_btn.clicked.connect(self.guest_login)
        
        layout.addWidget(self.login_entry,0,1)
        layout.addWidget(self.pass_entry,1,1)
        layout.addWidget(self.login_btn,2,0,1,2)
        layout.addWidget(self.guest_btn,3,0,1,2)
        
        self.show()
        
    def guest_login(self):
        self.bw = BaseWindow("гость","")
        self.bw.show()
    
    def password_login(self):
        user_input_login = self.login_entry.text().strip()
        user_input_password = self.pass_entry.text().strip()
        sql = "SELECT * FROM user_import WHERE `Логин`=%s"
        self.myDb.cur.execute(sql,(user_input_login,))
        ans = self.myDb.cur.fetchone()
        if ans is not None:
            if user_input_password == ans[3]:
                print("успех")
                self.role = ans[0]
                self.FIO = ans[1]
                self.bw = BaseWindow(self.role,self.FIO)
                self.bw.show()
            else:
                print("провл")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('login.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())
    