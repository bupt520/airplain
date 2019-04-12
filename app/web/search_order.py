# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         search_order
# Date:         2019/4/10
# -------------------------------------------------------------------------------
from datetime import datetime

from flask.json import jsonify

from app.data.order import MyOrder
from app.data.ticket import SearchTicket
from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.forms.search_order import SearchForm, OrderForm
from app.models.order import Order
from app.models.ticket import Ticket
from app.models.user import User, get_user
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():

        tickets = Ticket.query.filter_by(single_double=form.single_double.data, depart_date=form.depart_date.data,
                                         depart_city=form.depart_city.data, arrive_city=form.arrive_city.data).all()
        tickets = SearchTicket(tickets).tickets  # 列表包含着字典
        return '查询到tickets--------' + str(tickets)

    form.single_double.default = '往返'
    form.depart_date.default = datetime.now().strftime('%Y-%m-%d')
    form.process()
    return "获取搜索界面"
    # return render_template('web/search.html', form=form)


@web.route('/order/<plain_id>', methods=['GET', 'POST'])
def order(plain_id):
    order_id = 'P' + datetime.now().strftime('%Y%m%d%H%M%S')
    form = OrderForm(request.form)

    if request.method == 'POST':  # and form.validate():
        # < form action = "{{ url_for('web.order') ,plain_id=plain_id}}"method = "post" >
        with db.auto_commit():
            ticket = Ticket().query.filter_by(plain_id=plain_id).first()
            order = Order()
            order.order_id = form.order_id
            order.user_id = current_user.id  # userid = current_user.id, user = get_user(userid)
            order.ticket_type = form.ticket_type
            order.route = ticket.depart_city.data + '-' + ticket.arrive_city.data
            order.depart_time = ticket.depart_date.data + '-' + ticket.depart_time.data
            order.status = '正在处理'
            db.session.add(order)
            return redirect(url_for('web.my_order'))
    form.order_id.default = order_id
    form.process()
    return render_template('', form=form, plain_id=plain_id)

@web.route('/order/my')
def my_order():
    userid = current_user.id
    order=Order().query.filter_by(userid=userid).all()

    order = MyOrder(order).order
    return render_template('',order=order)

    pass

@web.route('/order/save')
def order_save():
    form = OrderForm(request.form)
    pass


# @web.route('/personalInfo', methods=['GET', 'POST'])
# def personal_info():
#     userid = current_user.id
#     user = get_user(userid)
#     # user = User.query.filter_by(id=userid).first()
#     return user.nickname
#
#
# @web.route('/changeInfo', methods=['GET', 'POST'])
# def change_info():
#     form = ChangeInfoForm(request.form)
#     if request.method == 'POST' and form.validate():
#         user = User.query.filter_by(nickname=form.nickname.data).first()
#         changed = user.change_info(form)
#
#         if changed:
#             return '用户信息更改成功'
#     return redirect(url_for('web.personal_info'))
