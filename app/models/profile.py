import sqlite3


def update_user_avatar(self, avatar, user_id):
    if not avatar:
        return False
    try:
        binary = sqlite3.Binary(avatar)
        self.__cur.execute(f'UPDATE users SET avatar = ? WHERE id = ?', (binary, user_id))
        self.__db.commit()
    except sqlite3.Error as e:
        print('Error of updating avatar in DB ' + str(e))
        return False
    return True