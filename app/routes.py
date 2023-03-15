from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


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