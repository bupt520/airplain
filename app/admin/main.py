# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         main
# Date:         2019/4/9
#-------------------------------------------------------------------------------
from flask import render_template, request

from app.forms.admin import AdminLoginForm
from . import admin

# 返回管理员登录视图
@admin.route('/admin')
def index():
    form=AdminLoginForm(request.form)
    return render_template('admin/AdminIndex.html',form=form)


@admin.route('/personal')
def personal_center():
    pass