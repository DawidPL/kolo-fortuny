import mysql.connector
from mysql.connector import Error

def add_word(category, title):
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'game'
        )
        cursor = connection.cursor(Buffered =  True)
        sql_query = '''INSERT INTO questions(category, title) VALUES (%s, %s)'''
        cursor.execute(sql_query, (category, title))
        print('Poprawnie dodano do bazy nowe pytania')
    except Error:
        print('MySQL connection error: {}'.format(Error))
    finally:
        if (connection.is_connected()):
            connection.close()

def get_name():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'game'
            )
        cursor = mydb.cursor()
        cursor.execute('SELECT user_name FROM questions')
        records = cursor.fetchone()
        for row in records:
            print ('Kategoria : ', row[1],)
        cursor.close()
    except Error:
        print('MySQL connection error: {}'.format(Error))
    finally:
        if (connection.is_connected()):
            mySQLconnection.close()

#cursor.execute('CREATE DATABASE game')
#cursor.execute('CREATE TABLE users(user_id INT PRIMARY KEY AUTO_INCREMENT, user_name VARCHAR(20))')
#cursor.execute('ALTER TABLE users ADD user_points INT DEFAULT(0)')

'''sql_insert_users = 'INSERT INTO users(user_name) VALUES (%s)'
names = [
    ('DAWID',), ('Ania',), ('Kasia',), ('Tomek',), ('Szymon',), ('Beata',), ('Wojtek',), 
    ('Ula',), ('Ola',), ('Piotrek',), ('Julia',), ('Zosia',), ('Łukasz',), ('Kuba',), ('Jagoda',),
]
cursor.executemany(sql_insert_users, names)
mydb.commit()'''

#sql_create_questions = 'CREATE TABLE questions(qs_id INT PRIMARY KEY AUTO_INCREMENT, category VARCHAR(50), title VARCHAR(100), if_used VARCHAR(1) DEFAULT(\'N\'))'
#sql_insert_questions = 'INSERT INTO questions(category, title) VALUES (%s, %s)'
words = [
    ('film', 'CZTEREJ PANCERNI I PIES'), ('film', 'KARMAZYNOWY PRZYPŁYW'), ('film', 'CZTERY WESELA I POGRZEB'),
    ('film', 'OGNIEM I MIECZEM'), ('film', 'ZAKOCHANY KUNDEL'),
]
#cursor.executemany(sql_create_questions, words)
#mydb.commit()
