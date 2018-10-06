#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from api.db import db
import web, json, datetime


class Api(Resource):
    def __init__(self):
        self.web = web.database(dbn='mysql', db='etl', user='root', pw='root', host='127.0.0.1', port=3306)
        self.db = db()

    def get(self):
        tmp_list = []
        # for row in self.web.query("select id,user_id,chinese_name,sex,phone from base_user_info limit 23"):
        # 如果数据库字段有日期或者时间类型，则无法转换成json格式，会报错
        # 解决方法：处理数据类型(序列化)，或者表的时间字段都用字符串吧
        for row in self.db.execute("select id,user_id,chinese_name,sex,phone,birthday from base_user_info limit 23"):
            print row
            tmp_list.append(row)
        data = {"data": tmp_list}
        return data
