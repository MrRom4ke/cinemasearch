from flask import Flask
from CinemaSearch.cinemasearch.app.config import ConfigFlask


def create_app():
    """
    Создает и конфигурирует Flask-приложение для проекта CinemaSearch.
    Returns:
    Flask: Flask-приложение, настроенное согласно настройкам из ConfigFlask.
    """
    app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')
    app.config.from_object(ConfigFlask)
    return app
