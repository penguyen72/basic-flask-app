import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    # This encrypts the cookies and session data related to website
    app.config["SECRET_KEY"] = 'super_secret_key'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite3:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    return app