# -*- coding: utf-8 -*-
import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.login import LoginPage
# Testecase是一个定好的测试框架。TestLogin是基于estCase的一个类
from pageobjects.logout import LogoutPage
from pageobjects.production_monitoring import ProductionMonitoringPage


class BaseTest(unittest.TestCase):

    url_msg_warning = "https://nccloud.weihong.com.cn/nccloudmes/view/msg_warming.html"

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        #self.login()
        self.loginByToken()

    def login(self):
        success = True
        driver = self.driver

        login_page = LoginPage(self.driver)
        login_page.type_login("18329030871","123456","520135")
        login_page.get_windows_img()  # 调用基类截图方法

        login_page.send_submit_btn()
        login_page.get_windows_img()  # 调用基类截图方法

        try:
            assert unicode('消息报警', "utf8")  in login_page.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def loginByToken(self):
        username = 'jmine'
        password = 'e10adc3949ba59abbe56e057f20f883e'
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiMTgzMjkwMzA4NzEiLCJleHAiOjE1MDg4MDMyMDAsImlhdCI6MTUwNjI0MzYzN30.T_dVzr7QHKKCXUw-0tEXJr490u8DvsDec0YEWuWrPMw'
        script = "var n={company:'维宏',email:'test@126.com',names:'lili',openid:'123456', phone:'18729030871',username:'" + username + "',password:'" + password + "',token:'" + token + "'};" + "window.localStorage.userData = JSON.stringify(n)"
        self.driver.execute_script(script)
        self.driver.get(self.url_msg_warning)

    def logout(self):
        sccess = True
        driver = self.driver
        #ALT+Enter导入LogoutPage这个类
        time.sleep(2)
        logout_page = LogoutPage(self.driver)
        logout_page.send_submit_btn()

    def tearDown(self):
        self.logout()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
