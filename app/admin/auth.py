# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         auth
# Date:         2019/4/11
#-------------------------------------------------------------------------------
from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.admin import Admin, get_user
from . import admin
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user

@admin.route('/admin/addAdmin', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            ad = Admin()
            ad.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(ad)
            return 'True'
    return ('False')
    #     return redirect(url_for('admin.login'))
    # return render_template('auth/register.html', form=form)


@admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        ad = Admin.query.filter_by(nickname=form.nickname.data).first()
        if ad and ad.check_passward(form.password.data):
            login_user(ad, remember=True)
            next = request.args.get('next')
            if not next:  # or not next.startwith('/'):
                next = url_for('admin.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return '用户已经登录'
    # return render_template('auth/login.html', form=form)


@admin.route('/admin/info', methods=['GET', 'POST'])
def personal_info():
    form = ChangeInfoForm(request.form)
    # 添加默认信息
    # def register(email=None, password=None):
    #     form = RegisterForm()
    #     form.email.default = email
    #     form.password.default = password
    #     form.process()
    #     ...
    #     return render_template('auth/register.html', form=form)
    userid = current_user.id
    ad = get_user(userid)
    form.nickname.default = ad.nickname
    form.password.default = ad.password
    form.name.default = ad.name
    form.id_card.default = ad.id_card
    form.phone_number = ad.phone_number
    form.process()
    # user = Admin.query.filter_by(id=userid).first()
    return form.phone_number


@admin.route('/changeInfo', methods=['GET', 'POST'])
def change_info():
    form = ChangeInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        ad = Admin.query.filter_by(nickname=form.nickname.data).first()
        changed = ad.change_info(form)

        if changed:
            return '用户信息更改成功'
    return redirect(url_for('admin.personal_info'))
