from flask import url_for, flash, redirect, render_template, make_response, request, g
from flask_login import current_user, logout_user
from CinemaSearch.cinemasearch import app


def profile_view():
    return render_template('profile.html')


def logout_view():
    logout_user()
    flash('You are has been successfully logout', 'success')
    return redirect(url_for('login'))


def userava_view():
    img = current_user.get_avatar(app)
    if not img:
        return ''

    h = make_response(img)
    h.headers['Content_Type'] = 'image/png'
    return h


def upload_view():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verify_ext(file.filename):
            try:
                img = file.read()
                res = g.update_user_avatar(img, current_user.get_id())
                if not res:
                    flash('Error of update avatar', 'error')
                    return redirect(url_for('profile'))
                flash('Avatar is updated', 'success')
            except FileNotFoundError as e:
                flash('Error of reading file', 'error')
        else:
            flash('Error of update avatar', 'error')
    return redirect(url_for('profile'))