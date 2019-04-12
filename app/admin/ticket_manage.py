# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket_manage
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from app.data.order import ManageOrder
from app.forms.admin import AddCompanyForm, AddTicketForm
from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.admin import Admin, get_user
from app.models.order import Order
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

@admin.route('/admin/order/manage', methods=['GET', 'POST','DELETE'])
def manage_order():
    order_id = request.args.get('order_id')
    if request.method == 'POST':# and form.validate():
        order = Order.query.filter_by(order_id).all()

        with db.auto_commit():
            order.status='已经处理'
            db.session.add(order)

            return '添加机票成功'
            # return redirect(url_for('web.login'))
    if request.method == 'DELETE':
        order = Order.query.filter_by(order_id).all()

        db.session.delete(order)
    # 显示所有的信息。

    order = Order.query.all()
    order = ManageOrder(order).order
    return render_template('',order=order)
