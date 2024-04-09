# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: db.py
@time: 2024/3/8 14:17
@desc:

"""
from model import *
from base_db import DB_POOL


class DB(object):
    """

    """

    pool = DB_POOL.load_options_from_settings("Docker Database", r'./config.ini')

    @staticmethod
    def add_data_for_model(model, info):
        """

        :param info:
        :return:
        """
        with DB.pool.get_session() as session:
            session.add(model(**info))

    @staticmethod
    def select_info_from_model(model, condition=None, limit=10):
        """

        :param model:
        :param condition:
        :param limit:
        :return:
        """
        with DB.pool.get_session() as session:
            query = session.query(model)
            if condition is not None:
                query = query.filter(condition)
            offset = 0
            while True:
                batch = query.offset(offset).limit(limit).all()
                if not batch:
                    break
                yield batch
                offset += limit

    @staticmethod
    def update_info_from_model(model, condition=None, info={}):
        """

        :param model:
        :param condition:
        :param info:
        :return:
        """
        with DB.pool.get_session() as session:
            return session.execute(update(model).where(condition).values(**info)).rowcount


if __name__ == '__main__':
    db = DB()
    # db.add_data_for_model(User,{
    #     "name": "188458764161",
    #     "password": "Fbb338791",
    #     "nick_name": "jhc2",
    #     "email": "JHC000abc@gmail.com",
    #     "cookie": "sadasdasweiouir1poi-01i4rq=-12`2o",
    # })
    #
    #
    # condition = and_(User.status == 0)
    # result = []
    # for user_lis in db.select_info_from_model(model=User, condition=None,limit=2):
    #     for user in user_lis:
    #         result.append(dict(user.__dict__))
    # print(result)

    # condition = and_(User.id > 0, User.status == 0)
    # for i in db.select_info_from_model(model=SignIn):
    #     print("i", i.id)

    # print(db.update_info_from_model(model=User, info={
    #     "nackname": "JB"
    # }, condition=(User.id == 3)))
