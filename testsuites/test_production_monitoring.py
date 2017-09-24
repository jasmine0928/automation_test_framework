# -*- coding: utf-8 -*-
import time
import unittest

# Testecase是一个定好的测试框架。TestLogin是基于estCase的一个类
from pageobjects.production_monitoring import ProductionMonitoringPage
from testsuites.base_test import BaseTest

class TestLogin(BaseTest):

     #使用test_下划线开头的方法，测试框架会自动调用这个方法
    def test_production_monitoring(self):
        sccess = True
        driver = self.driver
        # ALT+Enter导入LogoutPage这个类
        #调用生产监控页面
        production_monitoring_page = ProductionMonitoringPage(self.driver)

        #调用production_monitoring这个页面的click_production_monitoring_button方法
        production_monitoring_page.click_production_monitoring_button()
        #执行production_monitoring这个页面的click_lili_monitor方法
        production_monitoring_page.click_lili_monitor()
        production_monitoring_page.select_machines()
        #执行production_monitoring这个页面的click_all_remove_button方法
        #production_monitoring_page.click_all_remove_button()
        #执行production_monitoring这个页面的，add_all_monitor_paramsfan方法
        #production_monitoring_page.add_all_monitor_params()
        #production_monitoring_page.click_single_monitor_param()


if __name__ == '__main__':
    unittest.main()
