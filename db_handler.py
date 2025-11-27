import pymysql.cursors

class DB_handler():
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="kiselev",
                password="1234",
                database="pk41_demo"
            )
            self.cur = self.conn.cursor()
        except pymysql.Error:
            print("DB Error")