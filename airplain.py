# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         airplain
# Date:         2019/4/9
# -------------------------------------------------------------------------------


from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host='localhost', debug=app.config['DEBUG'], port=8000)
