from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class EditProfileForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired()])
     about_me = TextAreaField("About me", validators=[Length(min=0, max=140)])
     submit = SubmitField('Login')
class LoginForm(FlaskForm):
    '''Login Form'''
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Edit Profile')

class RegisterForm(FlaskForm):
    '''Login Form'''
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Post")
       