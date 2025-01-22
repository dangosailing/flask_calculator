from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from app.routes import bp

db = SQLAlchemy()

login_manager=LoginManager()
login_manager.login_view = "login"

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(
        Config
    )  # implement our config file into the flask config vars

    db.init_app(flask_app)
    login_manager.init_app(flask_app)
    flask_app.register_blueprint(bp)

    with flask_app.app_context():
        from app import routes, models
        db.create_all()

    return flask_app
