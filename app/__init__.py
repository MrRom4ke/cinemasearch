from flask import Flask, g
from .config import ConfigFlask
from .utils.manage_db import DatabaseManager
from .models.users import UsersRepo
from .models.menu import MenuRepo
from .routes import add_routes
from flask_sqlalchemy import SQLAlchemy
from .models.database_users import Users


def create_app():
    """
    Создает и конфигурирует Flask-приложение для проекта CinemaSearch.
    Returns:
    Flask: Flask-приложение, настроенное согласно настройкам из ConfigFlask.
    """
    app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
    app.config.from_object(ConfigFlask)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    with app.app_context():
        # Добавляем маршруты
        add_routes(app)

        # Добавляем менеджер для работы с БД
        db = SQLAlchemy(app)

        # Добавляем репозитории с объектом БД
        users_repo = UsersRepo(db)
        menu_repo = MenuRepo(db)
        database_users = Users(db)


        @app.before_request
        def before_request():
            """Установка соединения с БД перед запросом"""
            g.users_repo = users_repo
            g.menu_repo = menu_repo
            g.database_users = database_users

        @app.teardown_appcontext
        def close_db(error):
            """Закрываем соединение с БД, если оно было установлено"""
            db.close()

    return app
