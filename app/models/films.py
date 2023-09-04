class FilmRepo:
    """Репозиторий для работы с таблицей Films"""
    def __init__(self, db):
        self.db = db

    def get_new_film(self):
        """Получение новых фильмов"""
        try:
            res = self.db.execute('''SELECT * FROM films WHERE category = "new"''')
            if res:
                return res
        except:
            print('Error reading from DB')
        return []

    def get_top_film(self):
        """Получение top-10 фильмов"""
        try:
            res = self.db.execute('''SELECT * FROM films WHERE category = "top"''')
            if res:
                return res
        except:
            print('Error reading from DB')
        return []

    def get_soon_film(self):
        """Получение ещё не вышедших фильмов"""
        try:
            res = self.db.execute('''SELECT * FROM films WHERE category = "soon"''')
            if res:
                return res
        except:
            print('Error reading from DB')
        return []