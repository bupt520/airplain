# -*- coding: utf-8 -*-
"""
    File Name：    search
    Date：         2019/4/10
    Description :
"""
from wtforms import StringField, PasswordField, Form, SelectField, RadioField, DateField
from wtforms.validators import Length
from .base import DataRequired




class SearchForm(Form):
    # 查询机票表单
    cities = [('bj', '北京'), ('tj', '天津'), ('sh', '上海'), ('cq', '重庆'),
              ('gz', '广州'), ('qd', '青岛'), ('hz', '杭州'), ('wh', '武汉')]

    single_double = RadioField('航班类型', choices=[('单程', '单程'), ('往返', '往返')])
    depart_city = SelectField("出发城市", choices=cities, validators=[DataRequired(), Length(2, 10)])
    arrive_city = SelectField("到达城市", choices=cities, validators=[DataRequired(), Length(2, 10)])
    depart_date = DateField(label='出发日期', format='%Y-%m-%d')
    return_date = DateField(label='返程日期', format='%Y-%m-%d')


class OrderForm(Form):
    # 预订机票表单
    order_id = StringField('订单号', validators=[DataRequired()])
    ticket_type = SelectField('出发时间', choices=[(0, '经济舱'), (1, '商务舱'), (2, '头等舱')])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    phone_number = StringField('手机号码', validators=DataRequired())
    id_card = StringField('身份证号码', validators=DataRequired())
