from flask import Flask

from app.views.main import main_bp
from app.views.auth import auth_bp
from app.views.manager import manager_bp
from app.extensions import db, migrate, login_manager
from app.settings import config
from app.models import User, Category, File


def create_app(config_name=None):
    if config_name is None:
        config_name = 'development'

    app = Flask('app')

    app.config.from_object(config[config_name])

    register_extension(app)
    register_blueprints(app)

    return app


def register_extension(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(manager_bp, url_prefix='/manager')
