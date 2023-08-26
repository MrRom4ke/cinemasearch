from flask import render_template


def index():
    """Обработчик главной страницы"""
    return render_template('index.html')
