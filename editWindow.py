from PyQt6.QtWidgets import QApplication, QWidget, \
    QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QComboBox
from db_handler import DB_handler


class EditWindow(QWidget):
    def __init__(self, _shoe_obj):
        super().__init__()
        self.psevdo_id = _shoe_obj[0]
        layout = QGridLayout()
        self.setLayout(layout)
        #  интерфейс
        self.artikul = QLineEdit()
        self.artikul.setText(_shoe_obj[0])
        self.naimenovanie = QLineEdit()
        self.naimenovanie.setText(_shoe_obj[1])
        self.izmerenie = QLineEdit()
        self.izmerenie.setText(_shoe_obj[2])
        self.price = QLineEdit()
        self.price.setText(_shoe_obj[3])
        self.postav = QLineEdit()
        self.postav.setText(_shoe_obj[4])
        self.proizv = QLineEdit()
        self.proizv.setText(_shoe_obj[5])
        self.category = QLineEdit()
        self.category.setText(_shoe_obj[6])
        self.skidka = QLineEdit()
        self.skidka.setText(_shoe_obj[7])
        self.kolvo = QLineEdit()
        self.kolvo.setText(_shoe_obj[8])
        self.opisanie = QLineEdit()
        self.opisanie.setText(_shoe_obj[9])
        layout.addWidget(self.artikul, 0, 1)
        layout.addWidget(self.naimenovanie, 1, 1)
        layout.addWidget(self.izmerenie, 2, 1)
        layout.addWidget(self.price, 3, 1)
        layout.addWidget(self.postav, 4, 1)
        layout.addWidget(self.proizv, 5, 1)
        layout.addWidget(self.category, 6, 1)
        layout.addWidget(self.skidka, 7, 1)
        layout.addWidget(self.kolvo, 8, 1)
        layout.addWidget(self.opisanie, 9, 1)
        layout.addWidget(QLabel("артикул"), 0, 0)
        layout.addWidget(QLabel("наименование товара"), 1, 0)
        layout.addWidget(QLabel("Единица измерения"), 2, 0)
        layout.addWidget(QLabel("Цена"), 3, 0)
        layout.addWidget(QLabel("Поставщик"), 4, 0)
        layout.addWidget(QLabel("Производитель"), 5, 0)
        layout.addWidget(QLabel("Категория товара"), 6, 0)
        layout.addWidget(QLabel("Действующая скидка"), 7, 0)
        layout.addWidget(QLabel("Количество на складе"), 8, 0)
        layout.addWidget(QLabel("Описание"), 9, 0)
        self.edit_btn = QPushButton("Изменить")
        layout.addWidget(self.edit_btn, 10, 0, 1, 2)
        self.edit_btn.clicked.connect(self.edit_entry)

    def edit_entry(self):
        sql = f'''
        UPDATE tovar
        SET `Артикул` = %s, `Наименование товара`= %s, `Единица измерения`=%s,
            `Цена` = %s, `Поставщик` = %s, `Производитель` = %s, `Категория товара` = %s,
            `Действующая скидка` = %s, `Кол-во на складе` = %s,
            `Описание товара` = %s
        WHERE `Артикул`='{self.psevdo_id}';
        '''
        myDb = DB_handler()
        param = (self.artikul.text(), 
        self.naimenovanie.text(), self.izmerenie.text(),
        int(self.price.text()), self.postav.text(),
        self.proizv.text(), self.category.text(),
        int(self.skidka.text()), int(self.kolvo.text()),
        self.opisanie.text()
        )
        myDb.cur.execute(sql, param)
        myDb.conn.commit()
        self.close()
