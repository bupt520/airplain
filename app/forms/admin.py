# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         admin
# Date:         2019/4/11
# -------------------------------------------------------------------------------

from wtforms import StringField, PasswordField, Form, SelectField, SubmitField, RadioField, DateField, DateTimeField, \
    HiddenField, IntegerField
from wtforms.validators import Length, Email, ValidationError, EqualTo, Required
from .base import DataRequired

date_time = [(0, '全天'), (1, '07：00-23:59'), (2, '09：00-23:59'), (3, '11：00-23:59'), (4, '13：00-23:59'),
             (5, '15：00-23:59'), (6, '17：00-23:59'), (7, '19：00-23:59'), (8, '21：00-23:59'), (9, '23：00-23:59')]


class AdminLoginForm(Form):
    nickname = StringField('登录名', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('密码', validators=[DataRequired(),
                                               EqualTo('repeat_password'), Length(6, 20)])


class AddTicketForm(Form):
    # 下拉列表
    # status = SelectField('按类型查询', validators=[DataRequired()],
    #                      choices=[('0', '全部'), ('1', '待审核'), ('2', '认证成功'), ('3', '认证失败')])
    id = HiddenField('id')
    submit = SubmitField('Submit')

    single_double = RadioField('航班类型', choices=[(1, '单程'), (2, '往返')])
    name = StringField('航班名称', validators=[Length(2, 10)])
    company_name = StringField('航空公司', validators=[DataRequired(), Length(2, 10)])
    depart = StringField('出发城市', validators=[DataRequired(), Length(2, 10)])
    arrive = StringField('到达城市', validators=[DataRequired(), Length(2, 10)])

    depart_date = DateField(label='出发日期', format='%Y-%m-%d')
    depart_time = SelectField('出发时间', choices=date_time)
    arrive_date = DateField(label='到达时期', format='%Y-%m-%d')
    arrive_time = SelectField('到达时间', choices=date_time)
    return_date = DateField(label='返程日期', format='%Y-%m-%d')
    return_time = SelectField('返程时间', choices=date_time)

    first_class_price = IntegerField('头等舱价格')
    second_class_price = IntegerField('经济舱价格')
    third_class_price = IntegerField('商务舱价格')
    first_class_number = IntegerField('数量', validators=[DataRequired()])
    second_class_number = IntegerField('数量', validators=[DataRequired()])
    third_class_number = IntegerField('数量', validators=[DataRequired()])

    depart_ariport = StringField('出发机场')
    arrive_ariport = StringField('到达机场')


class AddAdminForm(Form):
    nickname = StringField('添加管理员账号', validators=[DataRequired(), Length(2, 10)])
    password = PasswordField('登录密码', validators=[DataRequired(),
                                                 EqualTo('repeat_password'), Length(6, 20)])
    repeat_password = PasswordField('确认密码', validators=[DataRequired(), Length(6, 20)])


class AddCompanyForm(Form):
    company_id = StringField('英文代号', validators=[DataRequired()])
    company_name = StringField('公司名称', validators=[DataRequired(), Length(2, 10)])


class ChangeCompanyForm(Form):
    company_id = StringField('英文代号')
    company_name = StringField('公司名称', validators=[DataRequired(), Length(2, 10)])
