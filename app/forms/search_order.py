# -*- coding: utf-8 -*-
"""
    File Name：    search
    Date：         2019/4/10
    Description :
"""
from datetime import datetime
from wtforms import StringField, PasswordField, Form, SelectField, RadioField, DateField
from wtforms.validators import Length
from .base import DataRequired


class SearchForm(Form):
    # 查询机票表单
    cities = [('北京', '北京'), ('天津', '天津'), ('上海', '上海'), ('重庆', '重庆'),
              ('广州', '广州'), ('青岛', '青岛'), ('杭州', '杭州'), ('武汉', '武汉')]
    single_double = RadioField('航班类型', choices=[('单程', '单程'), ('往返', '往返')])
    depart_city = SelectField("出发城市", choices=cities, validators=[DataRequired(), Length(2, 10)])
    arrive_city = SelectField("到达城市", choices=cities, validators=[DataRequired(), Length(2, 10)])
    depart_date = DateField(label='出发日期', format='%m/%d/%Y', default=datetime.now())
    return_date = DateField(label='返程日期', format='%m/%d/%Y')


class OrderForm(Form):
    # 预订机票表单
    order_id = StringField('订单号', validators=[DataRequired()])
    route = StringField('行程', validators=[DataRequired()])
    depart_time = StringField('起飞时间', validators=[DataRequired()])
    ticket_type = SelectField('机票类型', choices=[('经济舱', '经济舱'), ('商务舱', '商务舱'), ('头等舱', '头等舱')])
    name = StringField('姓名', validators=[DataRequired(), Length(1, 10)])
    phone_number = StringField('手机号码', validators=[DataRequired()])
    id_card = StringField('身份证号码', validators=[DataRequired()])
