# -*- coding: utf-8 -*-
"""
    File Name：    order
    Date：         2019/4/10
    Description :
"""
from sqlalchemy.orm import relationship, backref

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))  # 这个要不要定义一下一个外键，用户名

    order_id = Column(String(24), nullable=False)
    # create_time，调用create_datetime,然后.strftime('%Y-%m-%d %H:%M:%S')
    ticket_type = Column(String(24), nullable=False)
    route = Column(String(24), nullable=False)
    depart_time = Column(String(24), nullable=False)  # 2012.... 全天
    status = Column(String(24), nullable=False)  # 这个是“处理中”和“完成”。

    user = relationship('User', backref=backref('user_of_order'))

# class Company(Base):
#     __tablename__ = "company"
#     name = Column(String(20), primary_key=True)
#     location = Column(String(20))

# class Phone(Base):
#     __tablename__ = "phone"
#     id = Column(Integer, primary_key=True)
#     model = Column(String(32))
#     price = Column(String(32))
#     company_name = Column(String(32), ForeignKey("company.name"))
#     company = relationship("Company", backref="phone_of_company")
