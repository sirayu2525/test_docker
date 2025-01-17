#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, session
import mysql.connector, re
from datetime import timedelta



app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/event")
def event():
    return render_template('event.html')

@app.route("/event01")
def event01():
    return render_template('event01.html')

# uwsgiがこのapplicationオブジェクトを使ってアプリケーションを実行します
# application という名前で app をエイリアスします。uwsgi はデフォルトで application という名前のオブジェクトを探します。
# application = app

# if __name__ == "__main__":
#     app.run()
