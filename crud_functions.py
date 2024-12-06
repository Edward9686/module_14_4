import sqlite3


def initiate_db():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)''')

    products = [
        ('Продукт 1', 'Описание: Обычный стандарт круглых таблеток.', 100),
        ('Продукт 2', 'Описание: Интересные таблетки ввиде бобов.', 200),
        ('Продукт 3', 'Описание: Маленькие таблетки удобно пить.', 300),
        ('Продукт 4', 'Описание: Самые эффективные таблетки даже цвет зеленый.', 400)
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    connect.commit()
    connect.close()


def get_all_products():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()

    cursor.execute('''SELECT * FROM Products''')
    products = cursor.fetchall()

    connect.close()
    return products
