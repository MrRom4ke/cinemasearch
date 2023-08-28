from flask import request, render_template, flash, g
from werkzeug.security import generate_password_hash


def register_view():
    """Обработчик страницы регистрации"""
    if request.method == 'POST':
        if request.form['name'] and request.form['email'] and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = g.users_repo.add_user(request.form['name'], request.form['email'], hash)
            if res:
                flash('Зарегистрирован', 'success')
        else:
            flash('Не все данные введены верно', 'error')
    return render_template('register.html', title='Registration')

