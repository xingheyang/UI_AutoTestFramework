# project  :McenterSystem
# -*- coding = UTF-8 -*-
# Autohr   :XingHeYang
# File     :RegisterService.py
# time     :2020/11/28  14:46
# Describe : 注册流程
# ---------------------------------------
import allure
from page.RegisterPage import RegisterPage

@allure.feature("注册业务")
class RegisterService:

    def __init__(self,driver):
        self.reg = RegisterPage(driver)

    @allure.story("用户注册")
    def userRegister(self,account,username,password,repassword,issue,answer):
        self.reg.getRegisterPage()
        self.reg.inputAccount(account)
        self.reg.inputUsername(username)
        self.reg.inputPassword(password)
        self.reg.inputRepassword(repassword)
        self.reg.inputIssue(issue)
        self.reg.inputAnswer(answer)
        self.reg.clickSubmit()
        return self.reg.getalertText()