from flask import render_template, g


def index_view():
    """Обработчик главной страницы"""
    return render_template('index.html',
                           menu=g.menu_repo.get_menu(),
                           title='Главная страница',
                           new=g.film_repo.get_new_film(),
                           top=g.film_repo.get_top_film(),
                           soon=g.film_repo.get_soon_film()
                           )
