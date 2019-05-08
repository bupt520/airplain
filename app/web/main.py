# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         main
# Date:         2019/4/9
# -------------------------------------------------------------------------------
from flask import render_template, request, url_for

from app.data.ticket import SearchTicket
from app.forms.search_order import SearchForm
from app.models.ticket import Ticket
from . import web


@web.route('/')
def index():
    form = SearchForm(request.form)
    form.single_double.default = '往返'
    form.process()
    return render_template('web/index.html', form=form)

import os
from flask import send_from_directory

@web.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(web.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

