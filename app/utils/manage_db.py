import sqlite3


class DatabaseManager:
    def __init__(self, database_uri):
        self.database_uri = database_uri
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_uri)
            self.connection.row_factory = sqlite3.Row
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")
            return False

    def execute(self, query, params=None):
        if not self.connection:
            self.connect()

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка выполнения SQL-запроса: {e}")
            return None

    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def init_db(self):
        """Вспомогательная метод для создания таблиц в БД"""
        if self.connect:
            # Создание таблицы пользователей
            self.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                psw TEXT NOT NULL,
                time INTEGER NOT NULL
                );
            ''')

            # Создание меню
            self.execute('''
                CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL
                );
            ''')

            # Создание таблицы аватара
            self.execute('''
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                psw TEXT NOT NULL,
                avatar BLOB DEFAULT NULL,
                time INTEGER NOT NULL
                );
            ''')

            # Выполнение других запросов

            self.commit()
            self.close()
