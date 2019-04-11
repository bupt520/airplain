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
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_passward(self, raw):
        return check_password_hash(self._password, raw)

from app import login_manager
@login_manager.user_loader
def get_user(uid):
    return Admin.query.get(int(uid))