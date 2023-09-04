from flask import request, render_template, flash, g, url_for
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from CinemaSearch.cinemasearch.app.forms import forms



def register_view():
    """Обработчик страницы регистрации"""
    if request.method == "POST":
        # здесь должна быть проверка корректности введенных данных
        try:
            hash = generate_password_hash(request.form['psw'])
            u = Users(email=request.form['email'], psw=hash)
            db.session.add(u)
            db.session.flush()

            p = Profiles(name=request.form['name'],
                         old=request.form['old'],
                         city=request.form['city'],
                         user_id=u.id)
            db.session.add(p)
            db.session.commit()
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

        return redirect(url_for('index'))

    return render_template("register.html", title="Регистрация", form=forms)


def login_view():
    """Обработчик страницы авторизации"""
    pass

