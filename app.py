#!/usr/bin/env python
# coding=utf-8

from api import create_app

# 选择不同的模式启动
# mode=["default","development","testing","production"]
app = create_app("default")

if __name__ == "__main__":
    app.run()
