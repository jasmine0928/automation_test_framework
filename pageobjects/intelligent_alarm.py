# coding=utf-8
# 导入基类页面basepage
from framework.base_page import BasePage


# 定义一个生产监控页面
class IntelligentAlarmPage(BasePage):

    intelligent_alarmPage_link="xpath=>//*[@id='nav']/section/section/div/nav/ul/li[4]/a"
   # 下拉框
    add_Aparams_select= "xpath=>//*[@id='select_machine']/div[2]/span"
   # single_monitor_name,单击设备名
    single_machine_name="xpath=>//*[@id='select_machine']/div[2]/ul/li"


    # 超限报警
    overrun_alarm="xpath=>//*[@id='content']/section/section/div[2]/div/section/table/thead/tr/th[1]"
    # 主轴转速,注意
    min_spindleSpeed="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[1]/input[1]"
    max_spindleSpeed="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[1]/input[2]"
    #主轴倍率
    min_spindlefeedrate="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[2]/input[1]"
    max_spindlefeedrate="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[2]/input[2]"
    # 进给速度
    min_FeedV="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[3]/input[1]"
    max_FeedV="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[3]/input[2]"
    # 进给倍率
    min_whstatus_feedrate="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[4]/input[1]"
    max_whstatus_feedrate="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[3]/div[4]/input[2]"
    # 参数保存按钮
    saveAlarm_btn="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[4]"
    # 工作状态
    working_condition="xpath=>//*[@id='content']/section/section/div[2]/div/section/table/thead/tr/th[2]"
    # 超限报警中的远程按钮
    overrun_button="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[1]/div[4]/button"
    work_state="xpath=>//*[@id='content']/section/section/div[2]/div/section/table/thead/tr/th[2]"
    # 程序开始
    start_checkbox="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[2]/div[1]/div[1]/input"
    # 程序结束
    end_checkbox="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[2]/div[1]/div[2]/input"
    # 工作状态保存按钮
    saveStatus_button="xpath=>//*[@id='content']/section/section/div[2]/div/section/div[2]/div[2]"

   # 点击智能报警按钮
    def intelligent_alarmPageself(self):
        self.click(self.intelligent_alarmPage_link)
        self.sleep(2)
    # 选择设备
    def select_contents(self):
    # d点击下拉框
        #self.click(self.add_Aparams_select)
        #self.sleep(2)
        #当前默认选中的设备名称
        el = self.find_element("xpath=>//*[@id='select_machine']/div[2]/span")
        #这里错了。
        #如果选择的文字不等于'lili'：那么，1：点击选择的文字。2：选择lili。
        #el不能直接和字符串相加。要用el.text
        print 'default machine name:' + el.text
        if el.text != unicode('lili','utf8'):
            #1
            self.click(self.add_Aparams_select)
            #2
            self.click("xpath=>//*[@id='select_machine']/div[2]/ul/li[3]")
            self.sleep(2)

    # 点击超限报警
    def click_overrun_alarm_button(self):
        self.click(self.overrun_alarm)
        self.sleep(2)

    # 在主轴转速中输入最大值最小值
    def type_spindleSpeed(self,min,max):
        self.type(self.min_spindleSpeed,min)
        self.type(self.max_spindleSpeed,max)

    # 主轴倍率输入框中输入最大值、最小值
    def type_spindlefeedrate(self,min,max):
        self.type(self.min_spindlefeedrate, min)
        self.type(self.max_spindlefeedrate, max)

    # 进给输入输入框中输入最大值最小值
    def type_FeedV(self,min,max):
        self.type(self.min_FeedV, min)
        self.type(self.max_FeedV, max)

    # 进给倍率输入框中输入最大值最小值
    def type_whstatus_feedrate(self,min,max):
        self.type(self.min_whstatus_feedrate,min)
        self.type(self.max_whstatus_feedrate,max)
    # 点击参数设置保存
    def click_saveAlarm_btn(self):
        self.click(self.saveAlarm_btn)
        self.sleep(2)
    # 点击工作状态
    def click_work_state(self):
        self.click(self.work_state)
        self.sleep(2)
    # 设置程序开始
    def click_start_checkbox(self):
        self.click(self.start_checkbox)
        self.sleep(2)
    # 设置程序结束
    def click_end_checkbox(self):
        self.click(self.end_checkbox)
        self.sleep(2)
    # 点击工作状态中的保存
    def click_saveStatus_button(self):
        self.click(self.saveStatus_button)
        self.sleep(2)