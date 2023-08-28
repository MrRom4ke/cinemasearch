from flask import render_template, g


def index_view():
    """Обработчик главной страницы"""
    return render_template('index.html', menu=g.menu_repo.get_menu(), title='Главная страница')
