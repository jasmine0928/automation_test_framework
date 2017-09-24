# coding=utf-8
# 导入基类页面basepage
from framework.base_page import BasePage


class ZiDingYi(BasePage):
    # 自定义展板
    zidingyi_button = "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[6]/a"
    # 新建展板按钮
    newactive_button = "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[6]/ul/li/a"
    # 新建展板名字输入框
    newactivename_input = "xpath=>//*[@id='content']/div[2]/div[2]/input"
    # 取消按钮
    cancel_button = "xpath=>//*[@id='content']/div[2]/div[3]/button[1]"
    # OK按钮
    ok_button = "xpath=>//*[@id='content']/div[2]/div[3]/button[2]"
    # 自定义的新展板
    tempName_link = "xpath=>//*[@id='nav']/section/section/div/nav/ul/li[6]/ul/li[2]"
    # 添加自定义模块
    add_iconfont_button = "xpath=>//*[@id='content']/section/section/div/div[2]/section/div"
    # 设备选择下拉框
    select_machine = "xpath=>//*[@id='select_machine_container']"
    # 用于选择下拉框中所有的设备
    machines = "xpath=>//*[@id='select_machine_container']/ul/li"
    # 当前输入框的默认设备
    default_machine = "xpath=>//*[@id='select_machine_container']/span"
    # 当前设备选择框中的可选内容
    select_box_name = "xpath=>//*[@id='select_machine_container']/ul"

    # 内容选择下拉框
    select_parameterList = "xpath=>//*[@id='newTempParameters']"
    # 当前选择内容框中的默认内容
    default_patameter = "xpath=>//*[@id='newTempParameters']/span"
    # 下拉框中可选内容
    patameters = "xpath=>//*[@id='newTempParameters']/div[2]/ul/li"
    # lili设备下的参数名
    lili_name = "xpath=>//*[@id='WHNC-300A-GNGN-01BC']/section/h5/center"
    # 确定按钮
    queding_button = "class_name=>confirm_btn "
    # 删除展板按钮
    rmTemp_button = "xpath=>//*[@id='content']/div[1]/i"

    # 点击自定义展板下拉框
    def click_zidingyi_button(self):
        self.click(self.zidingyi_button)
        self.sleep(2)

    # 选择新建展板，点击
    def click_newactive_button(self):
        self.click(self.newactive_button)
        self.sleep(2)

    # 输入展板名，如果输入的展板名长度大于4位，截取前面四位，如果为空不能新建展板给出提示：新建展板名字不能为空!
    # 输入框的内容为特殊字符时，提示模板参数或模板名不能为空,模板名不能包含特殊字符
    def text_newactivename_input(self, name):
        self.type(self.newactivename_input, name)
        self.sleep(2)

    # 点击OK按钮
    def click_ok_button(self):
        self.click(self.ok_button)
        self.sleep(2)

    # 点击取消按钮
    def click_cancel_button(self):
        self.click(self.cancel_button)
        self.sleep(2)

    # 点击自定义设备展板
    def click_tempName_link(self):
        self.click(self.tempName_link)
        self.sleep(2)

    # 添加的展示块选择设备和内容
    def click_add_iconfont_button(self):
        self.click("class_name=>add")
        print 'dianji+'
        self.sleep(2)

    # 输入设备名
    def type_newactivename_input(self, name):
        self.type(self.newactivename_input, name)
        self.sleep(3)

    # 连续添加参数
    def add_machines(self):
        self.sleep(5)
        # 点击选择设备的下拉框,这一步是为了获取设备的个数
        self.click(self.select_machine)
        self.sleep(2)
        # 获取设备的长度
        size = len(self.find_elements(self.machines))
        # 当设备参数获取成功后，把获取成功的设备名添加到这步
        added = ''
        #再点击一下恢复原样
        self.click(self.select_machine)
        self.sleep(1)
        # x是从0到3的变量
        for x in range(0, size):
            #点击设备的下拉框
            self.click(self.select_machine)
            # 定位下拉框里面的所有设备元素
            elements = self.find_elements(self.machines)
            el = elements[x]
            # 如果元素没添加，那就点击这个元素，点击确定按钮。然后点击一下加号。然后再次重复该方法的操作，直到所有元素都添加进去。
            if el.text not in added:
                print 'will add machine:' + el.text
                # 点击过的元素加入added
                added += el.text
                machine = el.text
                el.click()
                self.sleep(1)
                self.add_parameters(machine)
                self.sleep(1)
                # 确定按钮
                # self.click("xpath=>/html/body/div/div[3]/button[2]")
                # 点击添加的加号
                self.sleep(1)
                # self.click_add_iconfont_button()
                # self.sleep(2)
                # 点击选择设备的下拉框
                # self.click(self.select_machine)
                # self.sleep(2)
                # 如果不满足，那就点击取消按钮。
        # 所有内容（设备名和参数内容）添加完后点击取消按钮
        self.click("xpath=>/html/body/div/div[3]/button[1]")
        self.sleep(2)

    #选择某个设备
    def machine(self, machine):
        self.sleep(1)
        # 点击选择设备的下拉框,这一步是为了获取设备的个数
        self.click(self.select_machine)
        self.sleep(1)
        # 获取设备的长度
        elements = self.find_elements(self.machines)
        size = len(elements)
        # 当设备参数获取成功后，把获取成功的设备名添加到这步
        for x in range(0, size):
            el = elements[x]
            if el.text == machine:
                el.click()
                break

    # 添加选择内容
    def add_parameters(self, machine):
        self.sleep(2)
        # 点击选择内容的下拉框,这一步是为了获取设备的个数
        self.click(self.select_parameterList)
        self.sleep(2)
        # 获取设备的长度
        size = len(self.find_elements(self.patameters))
        # 当参数获取成功后，把获取成功的设备名添加到这步
        added2 = ''
        self.click(self.select_parameterList)
        # x是从0到7的变量
        for x in range(0, size):
            # 定位下拉框里面的所有设备元素
            self.click(self.select_parameterList)
            elements = self.find_elements(self.patameters)
            el = elements[x]
            # 如果元素没添加，那就点击这个元素，点击确定按钮。然后点击一下加号。然后再次重复该方法的操作，直到所有元素都添加进去。
            if el.text not in added2:
                print 'will add patameter:' + el.text
                # 点击过的元素加入added
                added2 += el.text
                el.click()
                self.machine(machine)
                self.sleep(2)
                # 确定按钮
                self.click("xpath=>/html/body/div/div[3]/button[2]")
                # 点击添加的加号
                self.sleep(1)
                self.click_add_iconfont_button()
                self.sleep(2)

    # 点击确定
    def click_queding_button(self):
        self.click(self.queding_button)
        self.sleep(2)

    # 删除展板
    def click_rmTemp_button(self):
        self.click(self.rmTemp_button)
        self.click("xpath=>//*[@id='btnDialogBySHFConfirm']")
        self.sleep(2)