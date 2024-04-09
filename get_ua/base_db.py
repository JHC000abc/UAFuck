#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: base_db.py
@time: 2023/6/19 21:34
@desc:
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from sqlalchemy.pool import QueuePool
from base_tables import *
from model import *
from load_env import LoadINI
import traceback
import pymysql


class DB_POOL(object):
    """

    """

    def __init__(self, host, port, username, password, db, poll_size=50, debug=False):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.poll_size = poll_size
        # 初始化数据库连接池:
        self.engine = create_engine(f'mysql+mysqlconnector'
                                    f'://{self.username}:{self.password}'
                                    f'@{self.host}:{self.port}/{self.db}',
                                    poolclass=QueuePool, pool_size=self.poll_size,
                                    echo=True if debug else False
                                    )
        self.__create_db()
        # 创建线程安全的DBSession类型:
        self.db_session = scoped_session(sessionmaker(bind=self.engine, autocommit=False))

    @classmethod
    def load_options_from_settings(cls, name, file):
        """

        :param name:
        :param file:
        :return:
        """
        config = LoadINI.load_ini(name, file)
        return cls(config.get(name, "host"), config.getint(name, "port"), config.get(name, "username"),
                   config.get(name, "password"), config.get(name, "database"),debug=config.getboolean(name, "debug"))

    def __create_db(self):
        """
        新建表
        :return:
        """
        Base.metadata.create_all(self.engine, checkfirst=True)

    def run_origin_sql(self, session, sql):
        """
        执行原生sql
        :param session:
        :param sql:
        :return:
        """
        return session.execute(text(f"""{sql}"""))

    @contextmanager
    def get_session(self):
        """
        返回数据库连接对象
        :return:
        """
        session = self.db_session()
        try:
            yield session
            session.commit()
        except BaseException:
            session.rollback()
            raise
        finally:
            session.close()


class DB(object):
    def __init__(self, ip, port, user, password, db):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    @classmethod
    def load_options_from_settings(cls, name, file):
        """

        :param name:
        :param file:
        :return:
        """
        config = LoadINI.load_ini(name, file)
        return cls(config.get(name, "host"),config.getint(name, "port"),config.get(name, "username"),config.get(name, "password"),config.get(name, "database"))

    def __enter__(self):
        """

        :return:
        """
        self.conn = pymysql.connect(host=self.ip, port=self.port, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        try:
            self.conn.commit()
            self.cursor.close()
        except:
            self.conn.rollback()
            print(traceback.print_exc())
        finally:
            self.conn.close()


# if __name__ == '__main__':
#     db = DB.load_options_from_settings("Docker Database",r'../config.ini')
#     with db as cursor:
#         cursor.execute("show tables;")
#         print(cursor.fetchall())
#         cursor.execute("select * from user_info limit 10")
#         print(cursor.fetchall())