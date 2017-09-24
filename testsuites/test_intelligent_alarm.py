# -*- coding: utf-8 -*-
import time
import unittest

# Testecase是一个定好的测试框架。TestLogin是基于estCase的一个类,从pageobjects文件下的intelligent_alarm文件里调用IntelligentAlarmPage方法
from pageobjects.intelligent_alarm import IntelligentAlarmPage
from pageobjects.production_monitoring import ProductionMonitoringPage
from testsuites.base_test import BaseTest

class Test_alarm(BaseTest):

     #使用test_下划线开头的方法，测试框架会自动调用这个方法
    def test_intelligent_alarm(self):
        sccess = True
        driver = self.driver
        #把当前页面的title打印出来
        print driver.title
        # ALT+Enter导入LogoutPage这个类
        # 调用智能报警页面
        intelligent_alarm_page = IntelligentAlarmPage(self.driver)
        # 调用执行动作的方法
        intelligent_alarm_page.intelligent_alarmPageself()
        intelligent_alarm_page.select_contents()
        intelligent_alarm_page.click_overrun_alarm_button()
        intelligent_alarm_page.type_spindleSpeed("1000","9000")
        intelligent_alarm_page.type_spindlefeedrate("8000","10000")
        intelligent_alarm_page.type_FeedV("5000","6000")
        intelligent_alarm_page.type_whstatus_feedrate("2000","5000")
        intelligent_alarm_page.click_work_state()
        intelligent_alarm_page.click_start_checkbox()
        intelligent_alarm_page.click_end_checkbox()
        intelligent_alarm_page.click_saveStatus_button()

if __name__ == '__main__':
    unittest.main()
