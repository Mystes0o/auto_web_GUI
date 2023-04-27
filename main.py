# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# FileName:
# Author:      MingFeiyang
# Datetime:    2022/8/1 16:43
# Description：这个模块，用于执行测试套并生成测试报告
# -----------------------------------------------------------------------------------
import unittest
from time import strftime
from HTMLTestRunner import HTMLTestRunner
from common.read_ini import ReadIni


class EreTest:

    def run_ere(self):
        # 实例化测试条件对象 用于装测试用例
        suite = unittest.TestSuite()
        # 获取用例路径
        case_path = ReadIni().get_case_path()
        # 执行单个用例
        # suite.addTest(LoginTest('test_login_fail_2_amdin4343'))
        # 把用例装到测试套件中
        # 第一种方法 通过addTests来添加用例，通过TestLoader来加载用例，通过discover来找到用例，通过pattern来匹配用例
        # suite.addTests(unittest.TestLoader().discover(case_path, pattern="login_test.py"))
        # 第二种方法
        suite = unittest.defaultTestLoader.discover(case_path, pattern="*test.py")
        # 第三种方法
        # suite = unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest)

        # 执行测试套件来运行测试用例并生成测试报告
        # 利用第三方的生成报告的模块来生成报告
        # BeautifulReport(测试套)加载测试套件
        # run = BeautifulReport(suite)
        t = strftime("%Y_%m_%d_%H_%M_%S")
        # 运行测试套件生成测试报告
        # run.report(report_dir=ReadIni().get_report_path(), filename="ranzhi_report_{}.html".format(t),
        #            description="下面是然之项目的测试报告",theme='theme_cyan')

        # 用HTMLTestRunner来打印报告
        # 获取报告的绝对路径
        report = ReadIni().get_report_path() + "ranzhi_report_{}.html".format(t)
        with open(report, mode="w", encoding="utf8") as re:
            HTMLTestRunner.HTMLTestRunner(re, description="下面是然之项目的报告", title="然之测试报告").run(suite)


if __name__ == '__main__':
    run = RanzhiTest()
    run.run_ranzhi()
