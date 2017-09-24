# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

from framework.browser_engine import BrowserEngine
from pageobjects.login import LoginPage

#Testecase是一个定好的测试框架。TestLogin是基于estCase的一个类
from pageobjects.logout import LogoutPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
    def test_login(self):
        success = True
        driver = self.driver
        #driver.get("https://nccloud.weihong.com.cn/nccloudmes/view/login.html")

        login_page = LoginPage(self.driver)
        login_page.type_login("18329030871","123456","520135")
        login_page.send_submit_btn()


        try:
            assert unicode('消息报警', "utf8")  in login_page.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))



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
