# coding=utf-8
# 导入基类页面basepage
from framework.base_page import BasePage


# 定义一个生产监控页面
class ProductionMonitoringPage(BasePage):
    url = "https://nccloud.weihong.com.cn/nccloudmes/view/production_monitoring.html"
    production_monitoring_link = "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[2]/a"

    # 把lili这个设备放在monitor_lili_link里面
    monitor_lili_link = "selector_selector=>#WHNC-300A-GNGN-01BC"

    # 所有的remove button按钮
    all_remove_button = "class_name=>remove_btn"

    # 删除参数的确认按钮
    confirm_cancle_button = "id=>btnDialogBySHFConfirm"

    # 添加设备参数下拉框
    add_params_select = "xpath=>/html/body/div/div[1]/div[2]/span"

    # 添加参数的确定按钮
    confirm_add_button = "class_name=>confirm_btn"
    # 增加下拉框按钮
    select_button = "xpath=>/html/body/div/div[1]/div[2]/span"
    # 添加单个参数按钮
    single_monitor_param = "class_name=>confirm_btn"
    #定位单个参数
    single_param = "xpath=>/html/body/div/div[1]/div[2]/ul/li[3]"



    # 点击生产监控按钮
    def click_production_monitoring_button(self):
        self.click(self.production_monitoring_link)
        self.sleep(2)

    # 点击生产监控中的lili这个设备，定义click_lili_monitor这个方法
    def click_lili_monitor(self):
        print 'page title:' + self.get_page_title()
        self.click(self.monitor_lili_link)
        self.sleep(2)

    # 点击所有的移除按钮
    def click_all_remove_button(self):
        print 'page title:' + self.get_page_title()
        try:
            self.click(self.all_remove_button)
            self.click(self.confirm_cancle_button)
            self.sleep(2)
            self.click_all_remove_button()
        except Exception as e:
            print 'clicked all remove button.'
            return

    # 添加所有的设备参数
    def add_all_monitor_params(self):
        self.click("class_name=>addParameter")
        el = self.find_element(self.add_params_select)
        if el.text != unicode('没有可以添加的参数','utf8'):
            print 'add params ' + el.text
            #el.click()
            self.sleep(1)
            self.click(self.confirm_add_button)
            self.sleep(1)
            #循环调用add_all_monitor_params方法
            self.add_all_monitor_params()
        else:
            self.click("class_name=>abandon_btn")
            print 'added all params.'

    def click_single_monitor_param(self):
        self.click("class_name=>addParameter")
        el = self.find_element(self.add_params_select)
        if el.text == unicode('主轴转速','utf8'):
            self.click(self.single_monitor_param)
            self.sleep(2)
        else:
            self.click(self.select_button)
            self.click(self.single_param)
            self.click(self.single_monitor_param)
