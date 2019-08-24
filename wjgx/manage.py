# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:14:51 2019

@author: Yuhui_Zhang
"""
from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
