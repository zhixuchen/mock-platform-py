#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/4/10 9:57
# software: PyCharm
import os

if __name__ == '__main__':
    try:
        # print(os.system('%s' % ("pip freeze > requirements.txt")))#部署需要生成requirements.txt文件（宝塔部署需要修改生成文件内的Django 改为django）
        # print(os.system('%s' % ("py manage.py makemigrations")))
        # print(os.system('%s' % ("py manage.py migrate")))
        print(os.system('%s' % ("py manage.py runserver")))
        # print(os.system('%s' % ("py manage.py startapp safetest")))#创建新的APP注意修改url，settingT
    except Exception as e:
        print(e)
