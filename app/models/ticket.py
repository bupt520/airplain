# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         ticket
# Date:         2019/4/9
#-------------------------------------------------------------------------------

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float



class Ticket(Base):
    __tablename__ = 'ticket'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    name = Column(String(24), unique=True)
    phone_number = Column(String(18), unique=True)
    id_card = Column(String, unique=True)
    # gifts = relationship('Gift')

    _password = Column('password', String(128), nullable=False)