import sqlite3
import csv
cnx = sqlite3.connect('boots.sql')
cur = cnx.cursor()

# Step 2: Create a table

with open('Tovar.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  # Skip header row
    cur.executemany('INSERT INTO tovar (Артикул, Наименование_товара, Единица_измерения, Цена, Поставщик, Производитель, Категория_товара, Действующая_скидка, Кол_во_на_складе, Описание_товара, Фото) VALUES (?, ?,?,?,?,?,?,?,?,?,?)', csv_reader)

# Step 4: Commit changes and close the connection
cnx.commit()

# Step 5: Verify the data
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
cnx.close()
