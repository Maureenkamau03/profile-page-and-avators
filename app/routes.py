from app import app
from flask import render_template
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/aboutme')  
def aboutme():
    'About me URL'
    return render_template('aboutme.html', title="About me page") 

@app.route('/login')
def login():
    '''login url'''
    form = LoginForm()
    return render_template('login.html', title='login', form=form)     