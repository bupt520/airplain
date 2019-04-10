# -*- coding: utf-8 -*-
"""
    File Name：    order
    Date：         2019/4/10
    Description :
"""

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    single_double = Column(String, nullable=False)  # 单或双
    name = Column(String(24), unique=True)
    company_name = Column(String(24), nullable=False)
    depart = Column(String(24), nullable=False)
    arrive = Column(String(24), nullable=False)
    depart_date = Column(String(24), nullable=False)  # time
    depart_time = Column(String(24), nullable=False)
    arrive_date = Column(String(24), nullable=False)
    arrive_time = Column(String(24), nullable=False)
    return_date = Column(String(24))
    return_time = Column(String(24))
    first_class_price = Column(Integer, nullable=False)
    first_class_num = Column(Integer, nullable=False)
    second_class_price = Column(Integer, nullable=False)
    second_class_num = Column(Integer, nullable=False)
    third_class_price = Column(Integer, nullable=False)
    third_class_num = Column(Integer, nullable=False)
    depart_ariport = Column(String(24), nullable=False)
    arrive_ariport = Column(String(24), nullable=False)