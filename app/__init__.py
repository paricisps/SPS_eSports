from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

@app.template_filter('format_date')
def format_date(date):
    return date.strftime('%d/%m/%Y')

@app.template_filter('format_datetime')
def format_datetime(date):
    return date.strftime('%d/%m/%Y %I:%M %p')

@app.template_filter('format_time')
def format_time(date):
    return date.strftime('%I:%M %p')

from app import routes, models

