# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket_manage
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from flask import render_template, request, redirect, url_for, flash

from app.data.admin import CompanyInfo
from app.data.order import ManageOrder
from app.forms.admin import AddCompanyForm, AddTicketForm
from app.models.base import db
from app.models.order import Order
from app.models.ticket import Company, Ticket
from . import admin


@admin.route('/admin/test')
def test():
    return 'test'


# 请求和添加公司
@admin.route('/admin/company', methods=['GET', 'POST'])
def company():
    form = AddCompanyForm(request.form)
    companys = CompanyInfo(Company.query.all()).companys
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            company = Company()
            company.set_attrs(form.data)
            db.session.add(company)
            return redirect(url_for('admin.company'))
    return render_template('admin/CompanyManage.html', form=form, companys=companys)


# 修改删除公司
@admin.route('/admin/company/<company_name>', methods=['GET', 'POST'])
def change_company(company_name):
    form = AddCompanyForm(request.form)
    com=Company.query.filter_by(En_name=company_name).first()
    # if request.method == 'POST':  # and form.validate():

    if Ticket.query.filter_by(company_name=com.company_name).first():
        flash("WARNING!  该公司有关联的机票或订单，不能删除")
        return redirect(url_for('admin.company'))
    with db.auto_commit():
        db.session.delete(com)
    return redirect(url_for('admin.company'))


# 添加机票
@admin.route('/admin/ticket', methods=['GET', 'POST'])
def add_ticket():
    form = AddTicketForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            ticket = Ticket()
            ticket.set_attrs(form.data)
            db.session.add(ticket)
            return redirect(url_for('admin.add_ticket'))
    return render_template('admin/TicketAdd.html', form=form)


@admin.route('/admin/order/manage', methods=['GET', 'POST'])
def manage_order():
    order_id = request.args.get('order_id')
    if request.method == 'POST':  # and form.validate():
        order = Order.query.filter_by(order_id=order_id).first()

        with db.auto_commit():
            order.status = '已经处理'
            db.session.add(order)
            return redirect(url_for('admin.manage_order'))
    orders = Order.query.all()
    orders = ManageOrder(orders).order
    return render_template('admin/OrderManage.html', orders=orders)


@admin.route('/admin/order/dispose_order', methods=['POST'])
def dispose_order():
    order_id = request.args.get('order_id')
    with db.auto_commit():
        order = Order.query.filter_by(order_id=order_id).first()
        db.session.delete(order)
    return redirect(url_for('admin.manage_order'))
