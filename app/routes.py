from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/aboutme')  
def aboutme():
    'About me URL'
    return render_template('aboutme.html', title="About me page")  