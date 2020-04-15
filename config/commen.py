#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/4/16 11:13
# software: PyCharm
import os,configparser,json



def get_config(title,key):
    root_path=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))#项目路径
    ini_path=root_path+"/config/Config.ini"
    config = configparser.ConfigParser()
    config.read(ini_path,encoding='utf-8')
    result = config.get(title, key)
    return result


# def post(url,header,data):
#     headers = header
#     rep = requests.post(url=url, data=data, headers=headers)
#     post_result_json=json.loads(rep.text)
#     result=post_result_json
#     return result
#
# def get(url,header,params):
#
#     headers = header
#     rep = requests.get(url=url, params=params, headers=headers)
#     get_result_json = json.loads(rep.text)
#     result=get_result_json
#     return result