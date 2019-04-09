# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         user
# Date:         2019/4/9
# -------------------------------------------------------------------------------

from flask import current_app
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin
from app import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    name = Column(String(24), unique=True)
    phone_number = Column(String(18), unique=True)
    id_card = Column(String, unique=True)
    # gifts = relationship('Gift')

    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.load(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_passward(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
