# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket_manage
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from app.forms.admin import AddCompanyForm, AddTicketForm
from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.admin import Admin, get_user
from app.models.ticket import Company, Ticket
from . import admin
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user


@admin.route('/admin/test', methods=['GET', 'POST'])
def test():
    return 'admin test'

# 请求和添加公司
@admin.route('/admin/company', methods=['GET', 'POST'])
def company():
    form = AddCompanyForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            company = Company()
            company.set_attrs(form.data)
            db.session.add(company)
            return '添加公司成功'
            # return redirect(url_for('web.login'))
    return '请求添加公司'
    # return render_template('', form=form)

@admin.route('/admin/ticket', methods=['GET', 'POST'])
def ticket():
    form = AddTicketForm(request.form)
    if request.method == 'POST':# and form.validate():
        with db.auto_commit():
            ticket = Ticket()
            ticket.set_attrs(form.data)
            db.session.add(ticket)
            return '添加机票成功'
            # return redirect(url_for('web.login'))
    return '请求添加机票'