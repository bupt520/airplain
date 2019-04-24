# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         setting
# Date:         2019/4/9
# -------------------------------------------------------------------------------
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:mysql123@localhost:3306/airplain'
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://用户名:密码@localhost:3306/airplain'

SECRET_KEY = 'aqwrgsrtkj65476riqw34tare'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1518943695@qq.com'
MAIL_PASSWORD = 'xmbkzeoffythbahc'

# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5

SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = True

from datetime import timedelta

REMEMBER_COOKIE_DURATION = timedelta(days=30)
