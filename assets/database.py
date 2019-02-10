import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'game'
    )
my_cursor = mydb.cursor()

#my_cursor.execute('CREATE DATABASE game')
#my_cursor.execute('CREATE TABLE users(user_id INT PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(20))')
#my_cursor.execute('ALTER TABLE users ADD user_points INT DEFAULT(0)')

sql_insert = 'INSERT INTO users(user_name) VALUES (%s)'
records = [
    ('DAWID',), ('Ania',), ('Kasia',), ('Tomek',), ('Szymon',), ('Beata',), ('Wojtek',), 
    ('Ula',), ('Ola',), ('Piotrek',), ('Julia',), ('Zosia',), ('Łukasz',), ('Kuba',), ('Jagoda',),
]
my_cursor.executemany(sql_insert, records)
mydb.commit()

