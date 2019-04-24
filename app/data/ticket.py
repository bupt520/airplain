# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket
# Date:         2019/4/12
# -------------------------------------------------------------------------------

class SearchTicket():
    def __init__(self, raw_tickets):
        self.tickets = []
        self.raw_tickets = raw_tickets
        self.__parse()

    def __parse(self):
        for ticket in self.raw_tickets:
            temp_ticket = {}
            temp_ticket['name'] = ticket.name
            temp_ticket['company'] = ticket.company_name
            temp_ticket['depart_date_time'] = ticket.depart_date + ' ' + ticket.depart_time
            temp_ticket['arrive_date_time'] = ticket.arrive_date + ' ' + ticket.arrive_time
            temp_ticket['depart_airport'] = ticket.depart_airport
            temp_ticket['arrive_airport'] = ticket.arrive_airport

            temp_ticket['third_class_pric'] = '经济舱：' + str(ticket.third_class_price) + '元'
            temp_ticket['second_class_pric'] = '商务舱：' + str(ticket.second_class_price) + '元'
            temp_ticket['first_class_pric'] = '头等舱：' + str(ticket.first_class_price) + '元'

            temp_ticket['depart_city'] = ticket.depart_city
            temp_ticket['arrive_city'] = ticket.arrive_city
            self.tickets.append(temp_ticket)
