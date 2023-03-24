import os
import sqlite3

DATABASE_URL = os.environ.get('DATABASE_URL')

conn = sqlite3.connect(DATABASE_URL, uri=True)
cursor = conn.cursor()

# создание таблицы
cursor.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')
# вставка данных в таблицу
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# сохранение изменений
conn.commit()
# закрытие соединения
conn.close()
