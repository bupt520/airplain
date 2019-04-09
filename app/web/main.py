# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         main
# Date:         2019/4/9
#-------------------------------------------------------------------------------
from flask import render_template


from . import web


__author__ = '七月'


@web.route('/')
def index():
    return render_template('web/index.html')


@web.route('/personal')
def personal_center():
    pass