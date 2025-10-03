import sqlite3

class Db_handler:
    def __init__(self):
        self.cnx = sqlite3.connect('boots.sql')
        self.cur = self.cnx.cursor()
        #сделать проверку