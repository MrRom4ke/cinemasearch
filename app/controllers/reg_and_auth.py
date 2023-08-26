from flask import Flask, request, render_template, flash
from werkzeug.security import generate_password_hash


def register():
    """Обработчик страницы регистрации"""
    if request.method == 'POST':
        if request.form['name'] and request.form['email'] and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = database.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash('Зарегистрирован', 'success')
        else:
            flash('Не все данные введены верно', 'error')
    return render_template('register.html', title='Registration')

