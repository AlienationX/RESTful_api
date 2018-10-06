#!/usr/bin/env python
# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_NAME = basedir.split("/")[-1]
    APP_RESOURCES_FOLDER = "resources"
    MAIL_SERVER = ""
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    DB_DATABASE = "etl"
    # ENGINE_STR = "mysql+mysqldb://root:root@127.0.0.1:3306/{}?"
    ENGINE_STR = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}

if __name__ == "__main__":
    APP_NAME = basedir.split("/")[-1]
    print APP_NAME
