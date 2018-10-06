#!/usr/bin/env python
# coding=utf-8

from config import config
from sqlalchemy import create_engine, pool


def db():
    engine = create_engine(config["default"].ENGINE_STR, echo=False)  # ,poolclass=pool.NullPool
    conn = engine.connect()

    return conn


if __name__ == "__main__":
    conn = db()
    rows = conn.execute("select * from base_user_info limit 100")
    tmp_list = []
    for row in rows.fetchall():
        print row.items()
        print row["id"]
        tmp_list.append(row.keys())
    print {"rows": tmp_list}
