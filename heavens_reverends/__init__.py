import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import psycopg2
from flask_migrate import Migrate
from flask_login import LoginManager

# def get_env_variable(name):
#     try:
#         return os.environ[name]
#     except KeyError:
#         message = "Expected environment variable '{}' not set.".format(name)
#         raise Exception(message)

# the values of those depend on your setup
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
#######################
#### DATABASE SETUP
#######################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/heavens_reverends'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,
#                                                                pw=POSTGRES_PW,
#                                                                url=POSTGRES_URL,
#                                                                db=POSTGRES_DB)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from heavens_reverends.core.views import core
from heavens_reverends.error_pages.handlers import error_pages
from heavens_reverends.users.views import users
from heavens_reverends.posts.views import posts
from heavens_reverends.books.views import books
from heavens_reverends.appointments.views import appointments

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(books)
app.register_blueprint(appointments)
