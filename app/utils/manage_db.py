import sqlite3
from CinemaSearch.cinemasearch.app.config import ConfigFlask


def connect_db():
    """Подключение к БД"""
    try:
        conn = sqlite3.connect(ConfigFlask.DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print("Ошибка при подключении к базе данных:", e)
        return None


def init_db():
    """Вспомогательная функция для создания таблиц в БД"""
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()

        # Создание таблицы пользователей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            psw TEXT NOT NULL,
            time INTEGER NOT NULL
            );
        ''')

        # Выполнение других запросов

        conn.commit()
        conn.close()
