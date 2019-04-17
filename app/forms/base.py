# -*- coding: utf-8 -*-
"""
    File Name：    base
    Date：         2019/4/10
    Description :
"""

from flask import request
from wtforms import Form
from wtforms.validators import DataRequired as WTFDataRrequired


# from app.libs.error_message import FormException


class DataRequired(WTFDataRrequired):
    """
        重写默认的WTF DataRequired，实现自定义message
        DataRequired是一个比较特殊的验证器，当这个异常触发后，
        后续的验证（指的是同一个validators中的验证器将不会触发。
        但是其他验证器，比如Length就不会中断验证链条。
    """

    def __call__(self, form, field):
        if self.message is None:
            field_text = field.label.text
            self.message = field_text + '不能为空，请填写' + field_text
        super(DataRequired, self).__call__(form, field)


class BaseForm(Form):
    def __init__(self):
        body_data = request.form.to_dict()
        query_data = request.args.to_dict()
        super(BaseForm, self).__init__(**body_data, **query_data)

    def validate(self):
        # passed = super(BaseForm, self).validate()
        # if passed:
        #     return True
        # else:
        #     if request.accept_mimetypes.accept_json and \
        #             not request.accept_mimetypes.accept_html:
        #         raise FormException(self)
        pass
