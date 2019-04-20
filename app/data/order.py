# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         order
# Date:         2019/4/12
# -------------------------------------------------------------------------------
from app.models.user import User


class MyOrder():
    def __init__(self, raw_order):
        self.order = []
        self.raw_order = raw_order
        self.__parse()

    def __parse(self):
        for order in self.raw_order:
            temp_order = {}
            temp_order['order_id'] = order.order_id
            temp_order['order_time'] = order.create_datetime
            temp_order['ticket_type'] = order.ticket_type
            temp_order['route'] = order.route
            temp_order['depart_time'] = order.depart_time
            temp_order['status'] = order.status
            self.order.append(temp_order)


class ManageOrder():
    def __init__(self, raw_order):
        self.order = []
        self.raw_order = raw_order
        self.__parse()

    def __parse(self):
        for order in self.raw_order:
            user_id = order.user_id
            user = User.query.filter_by(id=user_id).first()
            temp_order = {}
            temp_order['order_id'] = order.order_id
            temp_order['order_time'] = order.create_datetime
            temp_order['ticket_type'] = order.ticket_type
            temp_order['route'] = order.route
            temp_order['depart_time'] = order.depart_time
            temp_order['status'] = order.status
            temp_order['user_name']=user.nickname
            # temp_order['user_name'] = order.user_of_order[0].nickname

            self.order.append(temp_order)
