# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: app.py
@time: 2024/4/9 11:47 
@desc: 

"""
from flask import Flask,request,render_template
import datetime, time
from model import *
from db import DB

app = Flask(__name__)
app.template_folder = './template'


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/upload',methods=['GET'])
def upload():
    ua = request.args.get('useragent')
    if ua:
        db = DB()
        _format = "%Y-%m-%d %H-%M-%S"
        time_now = time.strftime(_format, time.localtime())

        info = {
            "ua":ua,
            "update_time":time_now,
            "create_time":time_now
        }
        try:
            result = db.add_data_for_model(UaSave, info)
            return "Success"
        except:
            return "Failed"


if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=5000)
