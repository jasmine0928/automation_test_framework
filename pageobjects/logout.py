# coding=utf-8
#导入基类页面basepage
from framework.base_page import BasePage

#定义一个登录页面
class LogoutPage(BasePage):

    #下面三行分别是定位账号密码验证码的输入框，xpath
    logout_link= "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[7]/a/span"
    #logout_link = "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[7]/a"

    #发送登录信息
    def send_submit_btn(self):
        self.find_element(self.logout_link).click()
        #self.click(self.logout_link)
        self.sleep(3)
