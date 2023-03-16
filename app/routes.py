from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form =  RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'User {form.username.data} has been registered successfully.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/")
@app.route("/home")
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/aboutme')  
def aboutme():
    'About me URL'
    return render_template('aboutme.html', title="About me page") 

@app.route('/login', methods = ['GET', 'POST'])
@app.route('/login')
def login():
    '''login url'''
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'You are requesting to login {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='login', form=form)     