# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         auth
# Date:         2019/4/11
# -------------------------------------------------------------------------------
from app.data.admin import AdminInfo
from app.forms.admin import AddAdminForm
from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.admin import Admin, get_user
from . import admin
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user


@admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':  # and form.validate():
        ad = Admin.query.filter_by(nickname=form.nickname.data).first()
        if ad and ad.check_passward(form.password.data):
            login_user(ad, remember=True)
            next = request.args.get('next')
            if not next:  # or not next.startwith('/'):
                next = url_for('admin.manage')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('admin/AdminSignIn.html', form=form)


@admin.route('/admin/manage')
def admin_manage():
    form = AddAdminForm(request.form)
    admins = AdminInfo(Admin.query().all()).admins
    return render_template('admin/AdminIndex.html', form=form, admins=admins)


@admin.route('/admin/addAdmin', methods=['GET', 'POST'])
def add_admin():
    form = AddAdminForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            ad = Admin()
            ad.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(ad)
            return redirect(url_for('admin.admin_manage'))


@admin.route('/admin/changeInfo<nickname>', methods=['DELETE', 'POST'])
def change_info(nickname):
    form = AddAdminForm(request.form)
    form.nickname.default=nickname
    form.process()
    ad = Admin.query.filter_by(nickname=nickname).first()

    if request.method == 'POST':# and form.validate():
        changed = ad.change_info(form)
        if changed:
            print('管理员信息修改成功')
    if request.method == 'DELETE':
        with db.auto_commit():
            ad = Admin.query.filter_by(nickname=nickname).first()
            db.session.delete(ad)
    return redirect(url_for('admin.admin_manage'))
