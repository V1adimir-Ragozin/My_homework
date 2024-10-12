import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')

    for i in range(4):
        cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                       (f"Product{i+1}", f"Описание{i+1}", f"{(i+1)*100}"))


def get_all_products():
    products = cursor.execute("SELECT title, description, price FROM Products")
    a = []
    for i in products:
        a += {f'Название: {i[0]} | Описание: {i[1]} | Цена: {i[2]}'}
    connection.commit()
    return a
