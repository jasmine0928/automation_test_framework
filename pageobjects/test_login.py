# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_login(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(60)
    
    def test_test_login(self):
        success = True
        driver = self.driver
        driver.get("https://nccloud.weihong.com.cn/nccloudmes/view/login.html")
        driver.find_element_by_id("account").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("18329030871")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("codes").click()
        driver.find_element_by_id("codes").clear()
        driver.find_element_by_id("codes").send_keys("520135")
        driver.find_element_by_id("login").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
