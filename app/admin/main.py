# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         main
# Date:         2019/4/9
#-------------------------------------------------------------------------------
from flask import render_template


from . import admin

@admin.route('/')
def index():
    return render_template('admin/index.html')


@admin.route('/personal')
def personal_center():
    pass