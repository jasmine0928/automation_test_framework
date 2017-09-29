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
        driver = self.driver
        zidingyi_page = ZiDingYi(self.driver)
        # 循环添加自定义展板
        zidingyi_page.click_add_temps()
        # 点击自定义展板下拉框
        zidingyi_page.click_zidingyi_button()
        # 循环删除展板，
        zidingyi_page.click_rmTemps_button()
        # 点击新建展板按钮
        zidingyi_page.click_newactive_button()
        # 输入新建展板名字
        zidingyi_page.type_newactivename_input("235")
        # 点击新建展板成功后的OK按钮
        zidingyi_page.click_ok_button()
        driver = self.driver
        # j进入新建的展板
        zidingyi_page.go_tempName_link()
        # 添加的展示块选择设备和内容
        zidingyi_page.click_add_iconfont_button()
        # 对于某个展板，循环添加展板参数
        zidingyi_page.add_machines()
        zidingyi_page.click_rmTemp_button()


if __name__ == '__main__':
    unittest.main()

# global name 'el' is not defined
#意思就是el 未定义