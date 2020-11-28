# -*- coding = UTF-8 -*-
# Autohr   : yang
# File     : UtilsOperation.py
# project  : Python_project
# time     : 2020/11/16 17:01
# Describe : 工具类
# ---------------------------------------

import datetime
import os
import time


# 装饰用例的每个步骤，执行休眠操作
def _Sleep(func):
    def inner(*args):
        time.sleep(0.5)
        result = func(*args)
        time.sleep(0.5)
        return result

    return inner


def Sleep(s=1):
    def Sleep(func):
        nonlocal s

        def inner(*args):
            time.sleep(s)
            result = func(*args)
            time.sleep(s)
            return result

        return inner

    return Sleep


def createData(body="auto{}"):
    nowTime = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M")[2:]
    return body.format(nowTime)


def getPorjectPath():
    return os.path.dirname(os.path.dirname(__file__))


def ClearTestResult(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)
