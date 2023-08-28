class MenuRepo:
    """Репозиторий для работы с таблицей Menu"""
    def __init__(self, db):
        self.db = db

    def get_menu(self):
        """Получение меню из БД"""
        try:
            res = self.db.execute('''SELECT * FROM menu''')
            if res:
                return res
        except:
            print('Error reading from DB')
        return []
