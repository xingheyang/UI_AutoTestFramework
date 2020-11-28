# project  :Python_project
# -*- coding = UTF-8 -*-
# Autohr   : XingHeYang
# File     : conftest.py
# time     : 2020/10/9  11:03
# Describe :
# ---------------------------------------
import os
import sys
import time

import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import *
from config.config_box import browser_Config

data = Ini_File_Operation.read_Ini()

# 指定日志路径
log = GetLogger(data["conf"]["log"])
# 指定运行终端
Terminal = data["conf"]["Terminal"]
# 指定url
URL = data["conf"]["URL"]
# 错误截图路径
filepath = getPorjectPath() + data["conf"]["filepath"]

driver = None


@pytest.fixture(scope='session')
def driver():
    global driver
    log.info("测试开始：Terminal:%s URL:%s" % (Terminal, URL))
    driver = browser_Config(Terminal, URL)
    yield driver
    # driver.browser_close()


@pytest.fixture(scope="function")
def flush_browser(driver):
    driver.flush_browser()
    driver.sleep(1)


# 用例出现异常或失败时截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    picture_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filename = filepath + picture_time + ".png"
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver.base_driver.save_screenshot(filename)
            with open(filename, "rb") as f:
                file = f.read()
                allure.attach(file, "失败截图", allure.attachment_type.PNG)
