# project  :Python_Script
# -*- coding = UTF-8 -*-
# Autohr   :buxiubuzhi
# File     :config_box.py
# time     :2020/2/13  14:44
# Describe :
# ---------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import Ini_File_Operation, GetLogger, YamlOperation


class browser_Config:
    def __init__(self, Browser_type: str, url: str) -> None:
        """
        初始化浏览器，并输入地址
        :param Browser_type: 浏览器类型
        :param url: 需要打开的网址
        """
        if Browser_type == 'Chrome':
            self.base_driver = webdriver.Chrome()
        elif Browser_type == 'Firefox':
            self.base_driver = webdriver.Firefox()
        elif Browser_type == 'Ie':
            self.base_driver = webdriver.Ie()
        elif Browser_type == "Edge":
            self.base_driver = webdriver.Edge(executable_path="msedgedriver.exe")
        elif Browser_type == "PhantomJs":
            self.base_driver = webdriver.PhantomJS()
        elif Browser_type == 'ChromeOptions':
            option = webdriver.ChromeOptions()
            option.add_argument('--no-sandbox')
            option.add_argument('--headless')
            option.add_argument('--window-size=1920,1080')
            self.base_driver = webdriver.Chrome(options=option)
        else:
            raise Exception("Browser type Error")
        self.baseurl = url

    def __get(self, url: str) -> None:
        self.base_driver.get(url=url)
        self.implicitlyWait(10)
        self.base_driver.maximize_window()

    def get(self, url: str) -> None:
        urls = self.baseurl + url
        self.__get(urls)

    def implicitlyWait(self, s: int) -> None:
        """
        隐式等待
        :param s: 休眠时间，单位：秒
        :return:
        """
        self.base_driver.implicitly_wait(s)

    def sleep(self, s: float) -> None:
        """
        强制休眠
        :param s: 休眠时间
        :return:
        """
        time.sleep(s)

    def webdriver_wait(self, selector: str) -> None:
        """显示等待元素"""
        locator = self.__locate_Element_selector(selector)
        WebDriverWait(self.base_driver, 10, 0.5).until(
            EC.presence_of_element_located(locator))

    def __locate_Element_selector(self, selector: str) -> tuple:
        """
        八种定位方式选择
        :param selector: 传入的格式必须为：定位方式，定位元素值，顺序不可改变
        :return: 返回定位方式
        """
        selector_by = selector.split(',')[0].strip()
        selector_value = selector.split(',')[1].strip()
        if selector_by in ('i', 'id'):
            locator = (By.ID, selector_value)
        elif selector_by in ('n', 'name'):
            locator = (By.NAME, selector_value)
        elif selector_by in ('c', 'class'):
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by in ('x', 'xpath'):
            locator = (By.XPATH, selector_value)
        elif selector_by in ('s', 'css'):
            locator = (By.CSS_SELECTOR, selector_value)
        elif selector_by in ('t', 'tag_name'):
            locator = (By.TAG_NAME, selector_value)
        elif selector_by in ('l', 'link_text'):
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by in ('ll', 'partial_link_text'):
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        else:
            raise Exception('selector Error')
        return locator

    def locate_element(self, selector: str) -> WebElement:
        """
        定位单个元素
        :param selector: 定位元素的方式和定位元素的值
        :return: 返回定位元素对象
        """
        self.webdriver_wait(selector)
        locator = self.__locate_Element_selector(selector)
        element = self.base_driver.find_element(*locator)
        return element

    def locate_elements(self, selector: str) -> list:
        """
        定位一组元素值
        :param selector: 定位元素的方式和定位元素的值
        :return:
        """
        locator = self.__locate_Element_selector(selector)
        elements = self.base_driver.find_elements(*locator)
        return elements

    def element_click(self, selector: str) -> None:
        """元素点击操作"""
        ele = self.locate_element(selector)
        ele.click()

    def element_input(self, selector: str, value: str) -> None:
        """元素输入操作"""
        ele = self.locate_element(selector)
        ele.send_keys(value)

    def element_clear(self, selector: str) -> None:
        """元素输入框清空输入内容操作"""
        ele = self.locate_element(selector)
        ele.clear()

    def element_clear_input(self, selector: str, value: str) -> None:
        """清空输入框并输入内容"""
        ele = self.locate_element(selector)
        ele.clear()
        ele.send_keys(value)

    def get_element_text(self, selector: str) -> str:
        """获取元素文本内容"""
        ele = self.locate_element(selector)
        return ele.text

    def get_elements_text(self, selector: str) -> list:
        """获取一组元素的文本内容"""
        ele = self.locate_elements(selector)
        text_list = [i.text for i in ele]
        return text_list

    def get_elements(self, selector: str) -> list:
        """获取一组元素"""
        ele = self.locate_elements(selector)
        return ele

    def get_element_attribute(self, selector: str, value='value') -> str:
        """获取元素属性"""
        ele = self.locate_element(selector)
        return ele.get_attribute(value)

    def switch_frame_1(self, frame_name: str) -> None:
        """根据框架名称切换"""
        self.base_driver.switch_to.frame(frame_name)

    def switch_frame_2(self, selector: str) -> None:
        """根据框架定位元素值切换"""
        ele = self.locate_element(selector)
        self.base_driver.switch_to.frame(ele)

    def switch_parent_frame(self):
        """切换到父框架"""
        self.base_driver.switch_to.parent_frame()

    def switch_default_content(self):
        """切换到默认框架"""
        self.base_driver.switch_to.default_content()

    def switch_window(self, window_Num=-1):
        """切换窗口默认切换到最后一个"""
        handles = self.base_driver.window_handles()
        self.base_driver.switch_to.window(handles[window_Num])

    def operation_alert(self, operation='accept'):
        """处理弹窗"""
        alert = self.base_driver.switch_to.alert
        if operation == 'accept':
            alert.accept()
        elif operation == 'dismiss':
            alert.dismiss()

    def getAlertText(self):
        alert = self.base_driver.switch_to.alert
        return alert.text

    def select_operation(self, selector: str, operation_type: str, value: str) -> None:
        """下拉框处理"""
        if operation_type == 'index':
            Select(self.locate_element(selector)).deselect_by_index(value)
        elif operation_type == 'value':
            Select(self.locate_element(selector)).deselect_by_value(value)
        elif operation_type == 'text':
            Select(self.locate_element(selector)).deselect_by_visible_text(value)

    def browser_close(self):
        """关闭浏览器"""
        self.base_driver.close()

    def browser_quit(self):
        """退出浏览器"""
        self.base_driver.quit()

    def flush_browser(self):
        """刷新浏览器"""
        self.base_driver.refresh()

    def excute_script(self, script: str, element: str) -> None:
        """执行js脚本"""
        self.base_driver.execute_script(script, element)

    def exhibition_element(self, selector: str) -> None:
        """将元素显示到可见窗口中 """
        self.sleep(2)
        ele = self.locate_element(selector)
        js = "arguments[0].scrollIntoView();"
        self.excute_script(js, ele)


class box_Browser:
    module = ""

    def __init__(self, base_driver: browser_Config) -> None:
        self.base_driver = base_driver
        data = Ini_File_Operation.read_Ini()
        self.log = GetLogger(data[self.module]['log'])
        read_yaml = YamlOperation(data[self.module]['yaml'])
        self.selector = read_yaml.read_yaml()
