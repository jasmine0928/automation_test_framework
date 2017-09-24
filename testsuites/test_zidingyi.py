# -*- coding: utf-8 -*-
import time
import unittest

# Testecase是一个定好的测试框架。TestLogin是基于estCase的一个类
from pageobjects.zidingyi import ZiDingYi
from testsuites.base_test import BaseTest

class TestZiDingYi(BaseTest):
     # ALT+Enter导入LogoutPage这个类
     #使用test_下划线开头的方法，测试框架会自动调用这个方法
    def test_zidingyi(self):
        sccess = True
        zidingyi_page = ZiDingYi(self.driver)
        zidingyi_page.click_zidingyi_button()
        zidingyi_page.click_newactive_button()
        zidingyi_page.type_newactivename_input("lili")
        zidingyi_page.click_ok_button()
        driver = self.driver
        zidingyi_page.click_tempName_link()
        zidingyi_page.click_add_iconfont_button()
        zidingyi_page.add_machines()
        #zidingyi_page.click_rmTemp_button()

if __name__ == '__main__':
    unittest.main()

# global name 'el' is not defined
#意思就是el 未定义