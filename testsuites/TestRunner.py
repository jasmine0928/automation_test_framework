# coding=utf-8
import unittest

suite = unittest.TestLoader().discover("testsuites")

#这个是批量执行的函数。点击这个，testsuites文件夹下面的所有测试案例都会跑一遍。
if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    print suite
    runner.run(suite)