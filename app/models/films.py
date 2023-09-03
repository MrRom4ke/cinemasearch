class FilmRepo:
    """Репозиторий для работы с таблицей Films"""
    def __init__(self, db):
        self.db = db

    def get_film(self):
        """Получение фильмов"""
        try:
            res = self.db.execute('''SELECT * FROM films''')
            if res:
                return res
        except:
            print('Error reading from DB')
        return []