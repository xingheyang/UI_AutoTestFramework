# project  :McenterSystem
# -*- coding = UTF-8 -*-
# Autohr   :buxiubuzhi
# File     :RegisterPage.py
# time     :2020/11/28  14:36
# Describe : 注册页面
# ---------------------------------------
import allure
from config import *

class RegisterPage(box_Browser):

    module = "register"

    @Sleep()
    @allure.step("进入注册页面")
    def getRegisterPage(self):
        self.log.info("进入注册页面")
        self.base_driver.get(self.selector["REGISTER"])

    @Sleep()
    @allure.step("输入账号:{account}")
    def inputAccount(self,account):
        self.log.info("输入账号：%s"%account)
        self.base_driver.element_clear_input(self.selector["ACCOUNT"],account)

    @Sleep()
    @allure.step("输入用户名:{username}")
    def inputUsername(self,username):
        self.log.info("输入用户名：%s" % username)
        self.base_driver.element_clear_input(self.selector["USERNAME"],username)

    @Sleep()
    @allure.step("输入密码:{password}")
    def inputPassword(self,password):
        self.log.info("输入密码：%s" % password)
        self.base_driver.element_clear_input(self.selector["PASSWORD"],password)

    @Sleep()
    @allure.step("在次输入密码:{repassword}")
    def inputRepassword(self,repassword):
        self.log.info("在次输入密码：%s" % repassword)
        self.base_driver.element_clear_input(self.selector["REPASSWORD"],repassword)

    @Sleep()
    @allure.step("输入安全问题:{issue}")
    def inputIssue(self,issue):
        self.log.info("输入安全问题：%s" % issue)
        self.base_driver.element_clear_input(self.selector["ISSUE"],issue)

    @Sleep()
    @allure.step("输入答案:{answer}")
    def inputAnswer(self,answer):
        self.log.info("输入答案：%s" % answer)
        self.base_driver.element_clear_input(self.selector["ANSWER"],answer)

    @Sleep()
    @allure.step("点击提交")
    def clickSubmit(self):
        self.log.info("点击提交")
        self.base_driver.element_click(self.selector["SUBMIT"])
        
    @Sleep()
    @allure.step("获取注册后的弹窗文本")
    def getalertText(self):
        text = self.base_driver.getAlertText()
        self.log.info("弹窗的文本：%s"%text)
        return text
