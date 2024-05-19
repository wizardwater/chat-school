from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .connect import Connector
from flask_migrate import Migrate


def create_app():

    app = Flask(__name__)
    db_uri = Connector.read_config(section='postgres')  # read_config 함수를 호출하여 데이터베이스 URI를 가져옴
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy()
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import login
    app.register_blueprint(login.bp)

    return app