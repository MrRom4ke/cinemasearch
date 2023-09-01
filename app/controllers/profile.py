from flask import url_for, flash, redirect
from flask_login import current_user, logout_user


def profile_view():
    return f"""
            <p><a href="{url_for('logout')}">Log out</a>
            <p>User info: {current_user.get_id()}
            """

def logout_view():
    logout_user()
    flash('You are has been successfully logout', 'success')
    return redirect(url_for('login'))