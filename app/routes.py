from app import app, db
from app.models import User
from flask_login import login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.username.data}')
        # flash(f'You are requesting to login {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='login', form=form)

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
@login_required
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/<username>/profile')  
@login_required
def profile(username):
    'Profile page'
    user = user.query.filter_by(username=username).first_or_404()
    return render_template('profile.html',title='profile', title='Profile', user=user)
    return render_template('aboutme.html', title="About me page") 

# @app.route('/login', methods = ['GET', 'POST'])
# @app.route('/login')
# def login():
#     '''login url'''
#     form = LoginForm()

#     if form.validate_on_submit():
#         flash(f'You are requesting to login {form.username.data}')
#         return redirect(url_for('index'))
#     return render_template('login.html', title='login', form=form)     