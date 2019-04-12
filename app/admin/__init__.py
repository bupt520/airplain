# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         __init__.py
# Date:         2019/4/9
#-------------------------------------------------------------------------------
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)
# 下面不加也行
# from app.admin import admin
from app.admin import ticket_manage
from app.admin import auth
# from app.admin import drift
# from app.admin import gift
from app.admin import main
# from app.admin import wish
# from app.admin import user

@admin.app_errorhandler(404)
def not_found(e):
    # aop思想，面向切片编程，在每个出现问题的地方总结起来，集中起来
    return render_template('web/404.html'),404