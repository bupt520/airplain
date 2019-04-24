# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         search_order
# Date:         2019/4/10
# -------------------------------------------------------------------------------
from datetime import datetime

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from app.data.order import MyOrder
from app.data.ticket import SearchTicket
from app.forms.search_order import SearchForm, OrderForm
from app.models.base import db
from app.models.order import Order
from app.models.ticket import Ticket
from . import web


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST':  # and form.validate():

        tickets = Ticket.query.filter_by(single_double=form.single_double.data, depart_date=form.depart_date.data,
                                         depart_city=form.depart_city.data, arrive_city=form.arrive_city.data).all()
        tickets = SearchTicket(tickets).tickets  # 列表包含着字典
        return render_template('web/SearchResults.html', tickets=tickets, form=form)

    form.single_double.default = '往返'
    form.process()
    return render_template('web/SearchResults.html', form=form, tickets=[])


@web.route('/order/<plain_id>')
@login_required
def order(plain_id):
    """
    :param plain_id: 代表航班名称,name，需要前端返回。
    :return:
    """
    order_id = 'P' + datetime.now().strftime('%Y%m%d%H%M%S')
    form = OrderForm(request.form)
    ticket = Ticket.query.filter_by(name=plain_id).first()

    form.order_id.default = order_id
    form.route.default = ticket.depart_city + '-' + ticket.arrive_city
    form.depart_time.default = ticket.depart_date + '-' + ticket.depart_time
    form.process()
    return render_template('web/OrderInfo.html', form=form)


@web.route('/order/save_order', methods=['POST'])
@login_required
def save_order():
    form = OrderForm(request.form)
    if request.method == 'POST':  # and form.validate():
        with db.auto_commit():
            order = Order()
            order.set_attrs(form.data)
            # userid = current_user.id, user = get_user(userid)
            order.user_id = current_user.id
            order.status = '正在处理'

            db.session.add(order)
            return redirect(url_for('web.my_order'))


@web.route('/order/my')
@login_required
def my_order():
    user_id = current_user.id
    order = Order.query.filter_by(user_id=user_id).all()

    my_order = MyOrder(order).order
    return render_template('web/MyTicket.html', my_order=my_order)
