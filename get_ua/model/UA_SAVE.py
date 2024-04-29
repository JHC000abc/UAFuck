# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: UA_SAVE.py
@time: 2024/4/9 14:45 
@desc: 

"""
from .packages import *


class UaSave(Base):
    __tablename__ = 'ua_save'
    id = Column(INT, primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    ua = Column(VARCHAR(255), nullable=False, default="", unique=True)
    ip = Column(VARCHAR(255), nullable=False, default="", unique=True)
    update_time = Column(DateTime, server_default=func.now(), nullable=False)
    create_time = Column(DateTime, server_default=func.now(), nullable=False)

    __table_args__ = {
        'mysql_charset': 'utf8mb4'  # 设置字符集为utf8mb4
    }


DB_KDQ = "ua_save"
