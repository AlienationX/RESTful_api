#!/usr/bin/env python
# coding=utf-8

from flask_restful import Resource
from api.db import db


class Api(Resource):
    def __init__(self):
        self.db = db()

    def get(self):
        tb_names = []
        for row in self.db.execute("show tables"):
            tb_names.append(row[0])
        data = {"tables": tb_names}
        return data
