#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: load_env.py
@time: 2023/6/11 21:33
@desc:
"""
import os
from dotenv import load_dotenv
import configparser


class LoadEnv(object):
    """

    """
    def __init__(self):
        pass

    def load_env(self, key):
        """

        :param key:
        :return:
        """
        load_dotenv()
        args = os.getenv(key)
        if not args:
            raise ValueError("Not Found .env")
        else:
            return args


class LoadINI(object):
    """

    """
    def __init__(self):
        pass
    @staticmethod
    def load_ini(name=None, file="config.ini"):
        """

        :param name:
        :param file:
        :return:
        """
        config = configparser.ConfigParser()
        config.read(file, encoding="utf-8")
        # config.items(name)
        return config