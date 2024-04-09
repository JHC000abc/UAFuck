# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: app.py
@time: 2024/4/9 11:47 
@desc: 

"""
from flask import Flask,request,render_template

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
    db = DB()
    info = {
        "ua":request.args.get('useragent')
    }
    try:
        result = db.add_data_for_model(UaSave, info)
        return "Success"
    except:
        return "Failed"


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
