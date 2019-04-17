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

tickets = [
    {'name': '502次航班', 'company': '中国东方航空公司', 'depart_date_time': '2019-1-1 全天', 'arrive_date_time': '2019-1-1 12:00',
     'depart_airport': '北京', 'arrive_airport': '重庆', 'third_class_pric': '经济舱：1元', 'second_class_pric': '商务舱：2元',
     'first_class_pric': '头等舱：3元', 'depart_city': '北京', 'arrive_city': '重庆'},
    {'name': '1', 'company': '中国东方航空公司', 'depart_date_time': '2019-1-1 全天', 'arrive_date_time': '2019-1-1 12:00',
     'depart_airport': '北京', 'arrive_airport': '重庆', 'third_class_pric': '经济舱：1元', 'second_class_pric': '商务舱：2元',
     'first_class_pric': '头等舱：3元', 'depart_city': '北京', 'arrive_city': '重庆'}]


@web.route('/search', methods=['GET', 'POST'])
def search():
    searchform = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():

        # tickets = Ticket.query.filter_by(single_double=searchform.single_double.data, depart_date=searchform.depart_date.data,
        #                                  depart_city=searchform.depart_city.data, arrive_city=searchform.arrive_city.data).all()
        # tickets = SearchTicket(tickets).tickets  # 列表包含着字典
        return render_template('web/SearchResults.html', tickets=tickets, searchform=searchform)

    searchform.single_double.default = '往返'
    searchform.process()
    return render_template('web/index.html', orderform=searchform)


@web.route('/order/<plain_id>')
def order(plain_id):
    """
    :param plain_id: 代表航班名称,name，需要前端返回。
    :return:
    """
    order_id = 'P' + datetime.now().strftime('%Y%m%d%H%M%S')
    orderform = OrderForm(request.form)
    ticket = Ticket.query.filter_by(name=plain_id).first()

    orderform.order_id.default = order_id
    orderform.route.default = ticket.depart_city.data + '-' + ticket.arrive_city.data
    orderform.depart_time.default = ticket.depart_date.data + '-' + ticket.depart_time.data
    orderform.process()
    return render_template('web/OrderInfo.html', orderform=orderform)

@web.route('/order/save_order', methods=['POST'])
def save_order():
    form = OrderForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            order = Order()
            order.set_attrs(form)
            # userid = current_user.id, user = get_user(userid)
            order.user_id = current_user.id
            order.status = '正在处理'

            # order.order_id = form.order_id
            # order.ticket_type = form.ticket_type.data
            # order.route = form.route.data

            db.session.add(order)
            return redirect(url_for('web.my_order'))


@web.route('/order/my')
def my_order():
    user_id = current_user.id
    order = Order.query.filter_by(user_id=user_id).all()

    my_order = MyOrder(order).order
    return render_template('', my_order=my_order)




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
