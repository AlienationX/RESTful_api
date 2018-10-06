#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from api.db import db
import json


class Api(Resource):
    def __init__(self):
        self.db = db()

    def get(self):
        tb_names = []
        # for row in self.db.execute("show tables"):
        for row in self.db.execute("select * from base_user_info limit 23"):
            tb_names.append(row)
        data = {"tables": tb_names}
        return data
