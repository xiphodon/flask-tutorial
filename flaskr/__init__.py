#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:41
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : __init__.py
# @Software: PyCharm

import os
import click
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    if app.config['SECRET_KEY'] == 'dev':
        print('SECRET_KEY is dev')
    else:
        print('SECRET_KEY is Production')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app


# if __name__ == '__main__':
#     create_app(test_config=None).run(debug=True)
