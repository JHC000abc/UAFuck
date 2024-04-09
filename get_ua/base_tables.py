# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: base_tables.py
@time: 2023/12/9 21:57
@desc:

"""
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类,单写出来，避免循环引用
Base = declarative_base()
