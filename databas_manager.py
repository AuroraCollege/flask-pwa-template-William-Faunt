import sqlite3 as sql

from flask import render_template


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def index():
    data = listExtension()
    return render_template("/index.html", content=data)
