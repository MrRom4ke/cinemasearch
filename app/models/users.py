import math
import sqlite3
import time


class UsersRepo:
    """Репозиторий для работы с таблицей Users"""
    def __init__(self, db):
        self.db = db

    def add_user(self, name, email, hpsw):
        """Добавление нового пользователя в БД"""
        try:
            res = self.db.execute(f'SELECT COUNT() as "count" FROM Users WHERE email LIKE "{email}"')
            first_row = res[0]  # Получаем первую запись из результата
            count = first_row['count']  # Получаем значение 'count' из первой записи
            if count > 0:
                print('This user is already exists')
                return False
            tm = math.floor(time.time())
            self.db.execute('INSERT INTO users VALUES (NULL, ?, ?, ?, ?)', (name, email, hpsw, tm))
            self.db.commit()
        except sqlite3.Error as e:
            print('Error of adding user in DB ' + str(e))
            return False
        return True

    def get_user(self, user_id):
        """Идентифекация текущего пользователя"""
        try:
            self.db.execute(f'SELECT * FROM users WHERE id = {user_id} LIMIT 1')
            res = self.db.fetchone()
            if not res:
                print('User is not found')
                return False
            return res
        except sqlite3.Error as e:
            print('Error if getting data from DB ' + str(e))
        return False

    def get_user_by_email(self, email):
        try:
            self.db.execute(f'SELECT * FROM users WHERE email = "{email}" LIMIT 1')
            res = self.db.fetchone()
            if not res:
                print('User not found')
                return False
            return res
        except sqlite3.Error as e:
            print('Error of getting data from DB ' + str(e))
        return False
