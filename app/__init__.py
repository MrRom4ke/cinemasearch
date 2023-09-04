from flask import Flask, g
from .config import ConfigFlask
from .utils.manage_db import DatabaseManager
from .models.users import UsersRepo
from .models.menu import MenuRepo
from .routes import add_routes
from flask_sqlalchemy import SQLAlchemy


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
    database_users = SQLAlchemy(app)


    with app.app_context():
        # Добавляем маршруты
        add_routes(app)

        # Добавляем менеджер для работы с БД
        manager_db = DatabaseManager(ConfigFlask.DATABASE_PATH)

        # Добавляем репозитории с объектом БД
        users_repo = UsersRepo(manager_db)
        menu_repo = MenuRepo(manager_db)

        @app.before_request
        def before_request():
            """Установка соединения с БД перед запросом"""
            g.users_repo = users_repo
            g.menu_repo = menu_repo

        @app.teardown_appcontext
        def close_db(error):
            """Закрываем соединение с БД, если оно было установлено"""
            manager_db.close()

    return app
