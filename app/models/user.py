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
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nickname = Column(String(24), nullable=False)
    name = Column(String(24), unique=True)
    phone_number = Column(String(18), unique=True)
    id_card = Column(String(24), unique=True)

    _password = Column('password', String(128), nullable=False)

    def create_user(self, form):

        self.nickname = form.data['nickname']
        self.name = form.data['name']
        self.phone_number = form.data['phone_number']
        self.id_card = form.data['id_card']
        self.password = form.data['password']
        return self

    def change_info(self, form):

        with db.auto_commit():
            self.name = form.data['name']
            self.phone_number = form.data['phone_number']
            self.id_card = form.data['id_card']
            self.password = form.data['password']
            return True

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


from app import login_manager


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
