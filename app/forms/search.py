# -*- coding: utf-8 -*-
"""
    File Name：    search
    Date：         2019/4/10
    Description :
"""
from wtforms import StringField, PasswordField, Form
from wtforms.validators import Length, Email, ValidationError, EqualTo
from .base import DataRequired

class SearchForm(Form):
    nickname = StringField('用户名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), Length(6, 20)])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    id_card = StringField('身份证号码', validators=DataRequired())
    phone_number = StringField('手机号码', validators=DataRequired())