import pymysql.cursors


class DB_handler():
    """
    класс для подключения к базе данных.\n
    conn - параметр подключения к БД\n
    cur - параметр для создания запросов
    """
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
