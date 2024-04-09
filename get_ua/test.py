# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: test.py
@time: 2024/4/9 11:52 
@desc: 

"""
import requests

res = requests.get("http://172.25.148.124:5000/upload?useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
print(res.text)