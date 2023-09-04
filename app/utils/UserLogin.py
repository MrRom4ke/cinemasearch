from flask import url_for
from flask_login import UserMixin


class UserLogin(UserMixin):

    def get_avatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), 'rb') as f:
                    img = f.read()
            except FileNotFoundError as e:
                print('Default ava is not found ' + str(e))
        else:
            img = self.__user['avatar']
        return img


    def verify_ext(self, filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == 'png' or ext == 'PNG' or ext == 'Png':
            return True
        return False