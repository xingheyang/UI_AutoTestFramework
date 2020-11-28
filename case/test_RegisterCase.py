# project  :McenterSystem
# -*- coding = UTF-8 -*-
# Autohr   :XingHeYang
# File     :test_RegisterCase.py
# time     :2020/11/28  14:55
# Describe : 注册的测试用例
# ---------------------------------------
import allure
import pytest

from config.UtilsOperation import createData
from service.RegisterService import RegisterService


class TestRegister:
    
    @pytest.fixture(scope="function")
    def setUp(self,driver,flush_browser):
        self.reg = RegisterService(driver)


    @allure.title("用户注册")
    def testRegister(self,setUp):
        account = createData("account{}")
        result = self.reg.userRegister(account,account,"123456","123456","问题","答案")
        assert result == "注册成功,快去登录吧！"
        
