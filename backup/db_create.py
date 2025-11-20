import sqlite3
import hashlib

cnx = sqlite3.connect('boots.sql')
cur = cnx.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    Id INTEGER  PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT,
    role INTEGER
    )
 ''')

m = hashlib.sha256()
m.update(b"123")
password1 = m.hexdigest()
user1 = 'guest'
role1 = 1

m = hashlib.sha256()
m.update(b"client")
password2 = m.hexdigest()
user2 = 'client'
role2 = 2

m = hashlib.sha256()
m.update(b"manager")
password3 = m.hexdigest()
user3 = 'manager'
role3 = 3

m = hashlib.sha256()
m.update(b"admin")
password4 = m.hexdigest()
user4 = 'admin'
role4 = 4

sql= 'insert into users(login, password, role) values(?,?,?)'
values=[
    (user1, password1, role1),
    (user2, password2, role2),
    (user3, password3, role3),
    (user4, password4, role4)
]
cur.executemany(sql, values)
cnx.commit()
