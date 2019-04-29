# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         admin
# Date:         2019/4/11
# -------------------------------------------------------------------------------

from wtforms import StringField, PasswordField, Form, SelectField, SubmitField, RadioField, DateField, DateTimeField, \
    HiddenField, IntegerField
from wtforms.validators import Length, Email, ValidationError, EqualTo, Required

from app.models.ticket import Company
from .base import DataRequired


class AdminLoginForm(Form):
    nickname = StringField('登录名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])



class AddTicketForm(Form):
    date_time = [('全天', '全天'), ('07：00-23:59', '07：00-23:59'), ('09：00-23:59', '09：00-23:59'), ('11：00-23:59', '11：00-23:59'), ('13：00-23:59', '13：00-23:59'),
                 ('15：00-23:59', '15：00-23:59'), ('17：00-23:59', '17：00-23:59'), ('19：00-23:59', '19：00-23:59'), ('21：00-23:59', '21：00-23:59'), ('23：00-23:59', '23：00-23:59')]
    cities = [('北京', '北京'), ('天津', '天津'), ('上海', '上海'), ('重庆', '重庆'),
              ('广州', '广州'), ('青岛', '青岛'), ('杭州', '杭州'), ('武汉', '武汉')]

    id = HiddenField('id')
    submit = SubmitField('Submit')

    single_double = RadioField('航班类型', choices=[('单程', '单程'), ('往返', '往返')])
    name = StringField('航班名称', validators=[Length(2, 10)])
    company_name = SelectField(label="航空公司", validators=[DataRequired("请选择标签")])

    depart_city = SelectField("出发城市", choices=cities, validators=[DataRequired(), Length(2, 10)])
    arrive_city = SelectField("到达城市", choices=cities, validators=[DataRequired(), Length(2, 10)])

    depart_date = DateField(label='出发日期', format='%m/%d/%Y')
    depart_time = SelectField('出发时间', choices=date_time)
    arrive_date = DateField(label='到达时期', format='%m/%d/%Y')
    arrive_time = SelectField('到达时间', choices=date_time)
    return_date = DateField(label='返程日期', format='%m/%d/%Y')
    return_time = SelectField('返程时间', choices=date_time)

    first_class_price = IntegerField('头等舱价格')
    second_class_price = IntegerField('经济舱价格')
    third_class_price = IntegerField('商务舱价格')
    first_class_num = IntegerField('头等舱数量', validators=[DataRequired()])
    second_class_num = IntegerField('经济舱数量', validators=[DataRequired()])
    third_class_num = IntegerField('商务舱数量', validators=[DataRequired()])

    depart_airport = StringField('出发机场')
    arrive_airport = StringField('到达机场')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # company选择内容从数据库读取
        self.company_name.choices = [(c.company_name, c.company_name) for c in Company.query.all()]


class AddAdminForm(Form):
    nickname = StringField('添加管理员账号', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('登录密码', validators=[DataRequired(),
                                                 EqualTo('repeat_password'), Length(6, 20)])
    repeat_password = PasswordField('确认密码', validators=[DataRequired(), Length(6, 20)])


class AddCompanyForm(Form):
    En_name = StringField('英文代号', validators=[DataRequired()])
    company_name = StringField('公司名称', validators=[DataRequired(), Length(2, 10)])


class ChangeCompanyForm(Form):
    En_name = StringField('英文代号')
    company_name = StringField('公司名称', validators=[DataRequired()])
