# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         __init__.py
# Date:         2019/4/9
# -------------------------------------------------------------------------------

from flask import Blueprint, render_template

# from app.web import user

web = Blueprint('web', __name__)
# 下面不加也行
from app.web import main
from app.web import auth
from app.web import search_order


@web.app_errorhandler(404)
def not_found(e):
    # aop思想，面向切片编程，在每个出现问题的地方总结起来，集中起来
    return render_template('web/404.html'), 404
