# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         admin
# Date:         2019/4/17
#-------------------------------------------------------------------------------
class AdminInfo():
    def __init__(self,raw_admin):
        self.admins = []
        self.raw_admin = raw_admin
        self.__parse()


    def __parse(self):
        for admin in self.raw_admin:
            temp_admin = {}
            temp_admin['nickname']=admin.nickname
            temp_admin['role'] = admin.role
            self.admins.append(temp_admin)

            # id = Column(Integer, primary_key=True)
            # nickname = Column(String(24), nullable=False)
            # role = Column(String(24), nullable=False, default='超级管理员')
            # _password = Column('password', String(128), nullable=False)