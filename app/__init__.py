# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         __init__.py
# Date:         2019/4/9
# -------------------------------------------------------------------------------
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from app.models.base import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config')

    register_blueprint(app)

    db.init_app(app)

    mail.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # with app.app_context():
    #
    #     db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web import web
    from app.admin import admin
    app.register_blueprint(admin)
    app.register_blueprint(web)
