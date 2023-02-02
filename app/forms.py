from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanFiled
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    '''Login Form'''
    username = StringField('Username', validators=[DataRequired(), Lenght(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanFiled('Keep me logged in')
    submit = SubmitField('Login In')