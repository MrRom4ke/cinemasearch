from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email('Некорректный адрес!')])
    psw = PasswordField('Password: ', validators=[DataRequired(), Length(min=4, max=20, message='Пароль должен быть от 4 до 20 символов')])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Enter')


class RegisterForm(FlaskForm):
    name = StringField('Name:', validators=[Length(min=3, max=100, message='Name should be form 4 to 10 letters')])
    email = StringField('Email: ', validators=[Email('Некорректный адрес!')])
    psw = PasswordField('Password: ', validators=[DataRequired(), Length(min=4, max=20, message='Пароль должен быть от 4 до 20 символов')])
    psw2 = PasswordField('Repeat password ', validators=[DataRequired(), EqualTo('psw', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')