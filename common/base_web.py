# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# FileName:     base
# Author:      soozi
# Datetime:    2022/8/2 15:22
# Description：把webdriver封装
# -----------------------------------------------------------------------------------

import random

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec

# selenium 4
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_driver_path = ChromeDriverManager().install()  # 下载latest release版本的chromedriver，并返回其在本机的下载存储路径


# edge_driver_path = \


class Base:
    def __init__(self, browser, url=r"https://www.easeus.com/"):
        """
        构造方法，实现浏览器选择和打开，并窗口最大化，和隐式等待和输入被测网站
        :param browser: 浏览器名字，当前只支持谷歌和火狐
        :param url: 被测的网址
        """
        if browser == "c" or browser == "C" or browser == "Chrome":
            self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        elif browser == "f" or browser == "F" or browser == "Firefox":
            self.driver = webdriver.Firefox(service=Service(chrome_driver_path))
            raise NameError("请输入正确的浏览器名字！")

        self.driver.maximize_window()

        self.driver.implicitly_wait(30)

        self.driver.get(url)

    def _location_element(self, method, value, num="dan"):
        """
        定位元素
        :param method: 定位元素的方法：如id,name等
        :param value: 定位元素方法所对应的value值
        :param num: 单复数选择，默认为单
        :return: 定位到的元素
        """
        if method == "i" or method == "id":
            locator = (By.ID, value)
        elif method == "x" or method == "xpath":
            locator = (By.XPATH, value)
        elif method == "n" or method == "name":
            locator = (By.NAME, value)
        elif method == "s" or method == "css_elector":
            locator = (By.CSS_SELECTOR, value)
        elif method == "t" or method == "tag_name":
            locator = (By.TAG_NAME, value)
        elif method == "c" or method == "class_name":
            locator = (By.CLASS_NAME, value)
        elif method == "l" or method == "link_text":
            locator = (By.LINK_TEXT, value)
        elif method == "p" or method == "partial_link_text":
            locator = (By.PARTIAL_LINK_TEXT, value)
        else:
            raise NameError("请输入正确的定位方式")
        if num == "dan":
            return WebDriverWait(self.driver, 30, 1).until(ec.presence_of_element_located(locator))
            # return self.driver.find_element(*locator)  # *表示解包元组
        else:
            return WebDriverWait(self.driver, 30, 1).until(ec.presence_of_all_elements_located(locator))
            # return self.driver.find_elements(*locator)

    def send_keys(self, method, value, value1):
        """
        对定位到的元素进行输入操作
        :param method: 定位的方法
        :param value: 定位方法对象的value值
        :param value1: 要输入的内容
        :return: None
        """
        ele = self._location_element(method, value)
        ele.clear()
        ele.send_keys(value1)

    def click(self, method, value):
        """
        对定位到的元素进行点击操作
        :param method: 定位的方法
        :param value: 定位方法对象的value值
        :return: None
        """
        self._location_element(method, value).click()

    def get_text(self, method, value):
        """
        返回获取的文本值
        :param method: 定位的方法
        :param value: 定位方法对象的value值
        :return: 返回获取到的文本值
        """
        return self._location_element(method, value).text

    def switch_to_frame(self, method, value):
        """
        进入iframe框架
        :param method: 定位的方法
        :param value: 定位方法对象的value值
        :return: None
        """
        self.driver.switch_to.frame(self._location_element(method, value))

    def switch_to_parent_frame(self):
        """
        退到父级框架
        :return: None
        """
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        """
        退默认/最外层框架
        :return: None
        """
        self.driver.switch_to.default_content()

    def random_choice(self, method, value):
        """
        随机点击一个元素
        :param method: 定位的方法
        :param value: 定位方法对象的value值
        :return: None
        """
        eles = self._location_element(method, value, num="fd")
        random.choice(eles).click()

    def select_by(self, method1, value1, method, value):
        if method1 == "value":
            Select(self._location_element(method, value)).select_by_value(value1)
        elif method1 == "index":
            Select(self._location_element(method, value)).select_by_index(value1)

    def select_by_value(self, method, value, value1):
        """
        通过value值定位
        :param method: 定位方法
        :param value: 定位方法对应的值
        :param value1: 需要输入的value值
        :return: None
        """
        Select(self._location_element(method, value)).select_by_value(value1)

    def select_by_index(self, method, value, index):
        """
        通过value值定位
        :param method: 定位方法
        :param value: 定位方法对应的值
        :param index: 需要输入的索引
        :return: None
        """
        Select(self._location_element(method, value)).select_by_index(index)

    def select_by_visible_text(self, method, value, text):
        """
        通过value值定位
        :param method: 定位方法
        :param value: 定位方法对应的值
        :param text: 需要输入的文本
        :return: None
        """
        Select(self._location_element(method, value)).select_by_visible_text(text)

    def twice_location(self, method, value, by=By.TAG_NAME, value1="option"):
        """
        二次定位
        :param method: 父级的定位方法，用我们封装好的定位方法格式
        :param value: 父级定位方法对用的值
        :param by: 子级定位方法，用的底层格式  By.方法
        :param value1: 子级定位方法对应的值
        :return: None
        """
        eles = self._location_element(method, value).find_elements(by, value1)
        random.choice(eles).click()

    def twice_location1(self, by1=By.ID, value1=None, by2=By.TAG_NAME, value2="option"):
        """
        二次定位
        :param by1: 父级的定位方法，格式是By.方法
        :param value1: 父级定位方法对用的值
        :param by2: 子级定位方法，用的底层格式  By.方法
        :param value2: 子级定位方法对应的值
        :return: None
        """
        eles = self.driver.find_element(by1, value1).find_elements(by2, value2)
        random.choice(eles).click()

    def quit(self):
        self.driver.quit()

    def save_screenshot(self, filename):
        """
        获取截图
        :param filename: 截图保存的路径和名字
        :return: None
        """
        self.driver.save_screenshot(filename)

    def get_screenshot_as_file(self, filename):
        """
        获取截图
        :param filename:截图保存的路径和名字
        :return:None
        """
        self.driver.get_screenshot_as_file(filename)


if __name__ == '__main__':
    test = Base()