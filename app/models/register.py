import math
import sqlite3
import time


class RegisterBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_user(self, name, email, hpsw):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM Users WHERE email LIKE "{email}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('This user is already exists')
                return False
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO Users VALUES (NULL, ?, ?, ?, ?)', (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error of adding user in DB ' + str(e))
            return False
        return True
