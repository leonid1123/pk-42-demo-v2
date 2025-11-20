import pymysql.cursors

class DB_handler():
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="kiselev",
            password="1234",
            database="pk41_demo"
        )
        self.cur = self.conn.cursor()
