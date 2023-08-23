from app import create_app
from app.utils.manage_db import init_db


app = create_app()

if __name__ == "__main__":
    """
    Запускает Flask-приложение и инициализирует базу данных при запуске скрипта.
    """
    init_db()
    app.run()
