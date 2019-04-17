# -*- coding: utf-8 -*-
"""
    File Name：    user
    Date：         2019/4/10
    Description :
"""
from flask.json import jsonify

from app.forms.auth import RegisterForm, LoginForm, ChangeInfoForm
from app.models.user import User, get_user
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.models.base import db
from flask_login import login_user, logout_user, current_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    print(form.data, '#' * 100)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            # user=user.create_user(form)
            db.session.add(user)
            return 'True'
    # return ('False')
    #     return redirect(url_for('web.login'))
    return render_template('web/SignUp.html', form=form)


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
    # return '用户已经登录'
    return render_template('web/VIPSignIn.html', form=form)


@web.route('/personalInfo', methods=['GET', 'POST'])
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
    user = get_user(userid)
    form.nickname.default = user.nickname
    form.password.default = user.password
    form.name.default = user.name
    form.id_card.default = user.id_card
    form.phone_number = user.phone_number
    form.process()
    # current_user._get_current_object()

    # user = User.query.filter_by(id=userid).first()
    return render_template('web/MyTicket.html')


@web.route('/changeInfo', methods=['GET', 'POST'])
def change_info():
    form = ChangeInfoForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(nickname=form.nickname.data).first()
        changed = user.change_info(form)

        if changed:
            return '用户信息更改成功'
    return redirect(url_for('web.personal_info'))


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass
    # form = EmailForm(request.form)
    # if request.method == 'POST':
    #     if form.validate():
    #         account_email = form.email.data
    #         user = User.query.filter_by(email=account_email).first_or_404()
    #         from app.libs.email import send_email
    #         send_email(form.email.data, '重置你的密码', 'email/reset_password.html',
    #                    user=user, token=user.generate_token())
    #         flash('一封邮件已发送到' + account_email + '，请及时查收')
    # return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass
    # form = ResetPasswordForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     success = User.reset_password(token, form.password1.data)
    #     if success:
    #         flash('已经更新')
    #         return redirect(url_for('web.login'))
    #     else:
    #         flash('密码重置失败')
    # return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
