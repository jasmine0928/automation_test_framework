# coding=utf-8
#导入基类页面basepage
from framework.base_page import BasePage

#定义一个登录页面
class LoginPage(BasePage):

    #登录页面的地址
    url = "https://nccloud.weihong.com.cn/nccloudmes/view/login.html"
    #下面三行分别是定位账号密码验证码的输入框，xpath
    account_input = "xpath=>//*[@id='account']"
    password_input = "xpath=>//*[@id='password']"
    verify_code_input = "xpath=>//*[@id='codes']"
    #定义登录按钮
    login_button = "xpath=>//*[@id='login']"

    #输入登录的账号信息
    #定义一个函数def，type_login是自定义的。这个函数是用来输入登录条件信息的
    def type_login(self, name,password,codes): #self是loginpage的整个Class，必须要写。name，password,codes是定义了一个变量，实际的输入值是在test_login里
        # 这里是调用了基类定义的type方法。用来输入账号的。把name这个变量值输入到账号输入框中，name变量是test_login里面的账号值
        self.type(self.account_input, name)
        self.type(self.password_input, password)
        self.type(self.verify_code_input,codes)
        self.sleep(3)

    #发送登录信息
    def send_submit_btn(self):
        self.click(self.login_button)
        self.sleep(3)

