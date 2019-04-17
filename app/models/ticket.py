# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         ticket
# Date:         2019/4/9
# -------------------------------------------------------------------------------
from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey


class Company(Base):
    __tablename__ = 'company'
    company_name = Column(String(24), primary_key=True, nullable=False)
    id = Column(Integer, autoincrement=True)
    En_name = Column(String(24), nullable=False)  # 英语名字简写


class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    single_double = Column(String(4), nullable=False)  # 单或双
    name = Column(String(24), unique=True)
    company_name = Column(String(24), ForeignKey('company.company_name'), nullable=False)
    depart_city = Column(String(24), nullable=False)
    arrive_city = Column(String(24), nullable=False)
    depart_date = Column(String(24))  # time
    depart_time = Column(String(24))
    arrive_date = Column(String(24))
    arrive_time = Column(String(24))
    return_date = Column(String(24))
    return_time = Column(String(24))
    first_class_price = Column(Integer)
    first_class_num = Column(Integer)
    second_class_price = Column(Integer)
    second_class_num = Column(Integer, nullable=False)
    third_class_price = Column(Integer, nullable=False)
    third_class_num = Column(Integer, nullable=False)
    depart_airport = Column(String(24))
    arrive_airport = Column(String(24))

    company = relationship('Company', backref=backref('ticket_of_company'))
