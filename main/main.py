import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.UtilsOperation import ClearTestResult, getPorjectPath


def clearLogAndReport():
    print("----------清空上次测试结果----------")
    path = getPorjectPath() + "/result"
    ClearTestResult(path)
    time.sleep(2)
    print("----------测试结果清空成功----------")


def run(cases=" "):
    """运行case中所有用例"""

    clearLogAndReport()
    print("------------开始执行测试------------")
    cmd = "pytest " + getPorjectPath() + "/case/" + cases + " --alluredir " + getPorjectPath() + "/result/report"
    print(os.system(cmd))
    s = input("请选择要启用的服务:1:启动失败用例重跑;\t2：启动测试报告;")
    if s == "1":
        print("启动失败用例重跑")
        cmd = "pytest --lf " + getPorjectPath() + "/case/" + cases + " --alluredir " + getPorjectPath() + "/result/report"
        print(os.system(cmd))
        s = input("是否启动测试报告:y/n")
    if s == "2" or s == "y":
        print("-------------启动测试报告--------------")
        startReport = "allure serve " + getPorjectPath() + "/result/report"
        print(os.system(startReport))


run()
