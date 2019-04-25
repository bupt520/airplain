# -*- coding: utf-8 -*-
"""
    File Name：    admin
    Date：         2019/4/10
    Description :
"""

from flask import current_app
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    role = Column(String(24), nullable=False, default='super')
    password = Column('password', String(128), nullable=False)





    def check_passward(self, raw):
        return check_password_hash(self.password, raw)

    def change_info(self, form):
        with db.auto_commit():
            self.nickname = form.data['nickname']
            self.password = form.data['password']
            db.session.add(self)
            return True


# from app import login_manager
#
#
# @login_manager.user_loader
# def get_user(uid):
#     return Admin.query.get(int(uid))
