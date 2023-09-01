from flask import request, render_template, flash, g, redirect, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


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
    return render_template('register.html', menu=g.menu_repo.get_menu(), title='Registration')


def login_view():
    """Обработчик страницы авторизации"""
    if request.method == 'POST':
        user = db.get_user_email(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('index'))
        flash('Invalid username/password pair', 'error')
    return render_template('login.html', menu=db.get_menu(), title='Authorization')