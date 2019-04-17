# -*- coding: utf-8 -*-
"""
    File Name：    auth
    Date：         2019/4/10
    Description :
"""

# coding=utf-8
from wtforms import StringField, PasswordField, Form
from wtforms.validators import Length, Email, ValidationError, EqualTo
from .base import DataRequired
from app.models.user import User


class LoginForm(Form):
    nickname = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码')])


class RegisterForm(Form):
    nickname = StringField('用户名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), Length(6, 20)])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    id_card = StringField('身份证号码', validators=[DataRequired()])
    phone_number = StringField('手机号码', validators=[DataRequired()])

    def validate_id_card(self, field):
        if User.query.filter_by(id_card=field.data).first():
            raise ValidationError('身份证号已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class ChangeInfoForm(Form):
    nickname = StringField('用户名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    id_card = StringField('身份证号码', validators=[DataRequired()])
    phone_number = StringField('手机号码', validators=[DataRequired()])
