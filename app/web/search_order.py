# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         search_order
# Date:         2019/4/10
#-------------------------------------------------------------------------------

from flask.json import jsonify

from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.user import User, get_user
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user


@web.route('/search', methods=['GET', 'POST'])
def search():
    form = RegisterForm(request.form)
    print(form.data, '#' * 100)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(user)
            return 'True'
    return ('False')
    #     return redirect(url_for('web.login'))
    # return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        if user and user.check_passward(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next:  # or not next.startwith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return '用户已经登录'
    # return render_template('auth/login.html', form=form)


@web.route('/personalInfo', methods=['GET', 'POST'])
def personal_info():
    userid = current_user.id
    user = get_user(userid)
    # user = User.query.filter_by(id=userid).first()
    return user.nickname


@web.route('/changeInfo', methods=['GET', 'POST'])
def change_info():
    form = ChangeInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        changed = user.change_info(form)

        if changed:
            return '用户信息更改成功'
    return redirect(url_for('web.personal_info'))