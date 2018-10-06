#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource, reqparse
from api.db import db
import json


class Api(Resource):
    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument("mode", type=str, help="过滤默认的数据库")
        # self.get_args.add_argument('ids', type=str)
        # self.get_args.add_argument('dtype', type=str, required=True, help="dtype cannot be blank!")
        # self.get_args.add_argument('wtype', type=str, required=True, help="wtype cannot be blank!")
        # self.get_args.add_argument('cityid', type=str)
        # self.get_args.add_argument('areaid', type=str)
        # self.get_args.add_argument('brandid', type=str)
        # self.get_args.add_argument('dt', type=str)
        # self.get_args.add_argument('code', type=str)
        # self.get_args.add_argument('version', type=str)
        # self.get_args.add_argument('appid', type=str)
        # self.get_args.add_argument('regionid', type=str)
        self.args = self.get_args.parse_args()
        self.db = db()

    def get(self):
        mode = self.args["mode"]

        db_names = []
        sql = "show databases"
        for row in self.db.execute(sql):
            db_names.append(row[0])
        if mode == "filter":
            db_names = [x for x in db_names if x not in ("mysql", "sys", "information_schema", "performance_schema")]
        data = {"databases": db_names}
        return data
