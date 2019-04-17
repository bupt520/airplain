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
    loginform = LoginForm(request.form)
    if request.method == 'POST':  # and loginform.validate():
        ad = Admin.query.filter_by(nickname=loginform.nickname.data).first()
        if ad and ad.check_passward(loginform.password.data):
            login_user(ad, remember=True)
            next = request.args.get('next')
            if not next:  # or not next.startwith('/'):
                next = url_for('admin.manage')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('admin/AdminSignIn.html', loginform=loginform)


@admin.route('/admin/manage')
def admin_manage():
    adminform = AddAdminForm(request.form)
    admins = AdminInfo(Admin.query().all()).admins
    return render_template('admin/AdminIndex.html', adminform=adminform, admins=admins)


@admin.route('/admin/addAdmin', methods=['GET', 'POST'])
def add_admin():
    adminform = AddAdminForm(request.form)
    if request.method == 'POST' and adminform.validate():
        with db.auto_commit():
            ad = Admin()
            ad.set_attrs(adminform.data)
            # user=user.create_user(form)
            db.session.add(ad)
            return redirect(url_for('admin.admin_manage'))


@admin.route('/admin/changeInfo<nickname>', methods=['DELETE', 'POST'])
def change_info(nickname):
    change_admin_form = AddAdminForm(request.form)
    change_admin_form.nickname.default=nickname
    change_admin_form.process()
    ad = Admin.query.filter_by(nickname=nickname).first()

    if request.method == 'POST':# and change_admin_form.validate():
        changed = ad.change_info(change_admin_form)
        if changed:
            print('管理员信息修改成功')
    if request.method == 'DELETE':
        with db.auto_commit():
            a = Admin.query.filter_by(nickname=nickname).delete()
            print(a)
    return redirect(url_for('admin.admin_manage'))
