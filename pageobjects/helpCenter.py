# coding=utf-8
# 导入基类页面basepage
from framework.base_page import BasePage


class HelpCenter(BasePage):
   helepcenter_link="xpath=>//*[@id='nav']/section/section/div/nav/ul/li[5]/a"
   search_type="xpath=>//*[@id='content']/section/section/div[2]/div/div/input"
   searchPage_button="xpach=>//*[@id='searchHelp']"
   searchAll_button="xpath=>//*[@id='content']/section/section/div[2]/div/div/div/input"
   goback_button="xpath=>//*[@id='helpBack']"
   # 列表
   levels="xpath=>//*[@id='content']/section/section/div[3]/div[2]/section/ul/li"

