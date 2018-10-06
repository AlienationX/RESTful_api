#!/usr/bin/env python
# coding=utf-8

"""
    router设置等等
"""

from flask import Flask, make_response
from flask_restful import Api
from config import config
import os
import json


# from api.resources import databases, tables


def create_app(config_name):
    app = Flask(__name__)
    app.debug = config[config_name].DEBUG
    app_name = config[config_name].APP_NAME
    app_resources_folder = config[config_name].APP_RESOURCES_FOLDER
    api = Api(app)

    # api.representation["application/json"] = output_json

    resources = os.listdir(os.path.join(os.path.dirname(__file__), app_resources_folder))
    for resource in resources:
        if resource == "__init__.py" or resource[-3:] != ".py":
            continue
        else:
            resource = resource[:-3]
        model_string = "{}.{}.{}".format(app_name, app_resources_folder, resource)
        print model_string
        # model_name = __import__(model_string, globals(), locals(), "Api")
        model_name = __import__(model_string, fromlist=[resource])
        url_name = "/{app_name}/v1/resources/{resource}".format(app_name=app_name, resource=resource)
        class_name = resource.capitalize()
        print model_name, url_name, class_name
        api.add_resource(model_name.Api, url_name, endpoint=class_name)
    # api.add_resource(databases.Api, '/api/v1/resources/databases', endpoint="Databases")
    # api.add_resource(tables.Api, '/api/v1/resources/tables', endpoint="Tables")

    return app

# @api.representation('application/json')
# def output_json(data, code, headers=None):
#     resp = make_response(json.dumps(data), code)
#     resp.headers.extend(headers or {})
#     return resp
