#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 16:10
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : test_factory.py
# @Software: PyCharm

from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
