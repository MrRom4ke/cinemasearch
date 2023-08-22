from flask import Flask, request, render_template, flash
from werkzeug.security import generate_password_hash

from CinemaSearch.cinemasearch.wsgi import app


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['name'] and len(request.form['Nick']) > 3 and request.form['email'] and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = database.addUser(request.form['name'], request.form['Nick'], request.form['email'], hash)
            if res:
                flash('Зарегистрирован', 'success')
        else:
            flash('Не все данные введены верно', 'error')
    return render_template('register.html', title='Registration')

