from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config.from_object(Config)

#objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models