# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         __init__.py
# Date:         2019/4/9
# -------------------------------------------------------------------------------
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from werkzeug.security import generate_password_hash

from app.models.admin import Admin
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

    # 第一次运行成功之后可以把34-45行注释掉
    with app.app_context():

        db.create_all(app=app)
        if not Admin.query.filter_by(nickname='admin').first():
            ad = Admin()
            ad.nickname = 'admin'
            ad.role = 'super'
            ad.password = generate_password_hash('123456')

            with db.auto_commit():
                db.session.add(ad)
    return app


def register_blueprint(app):
    from app.web import web
    from app.admin import admin
    app.register_blueprint(admin)
    app.register_blueprint(web)
