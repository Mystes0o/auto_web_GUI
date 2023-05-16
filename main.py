# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# FileName:
# Author:      MingFeiyang
# Datetime:    2022/8/1 16:43
# Description：这个模块，用于执行测试套并生成测试报告
# -----------------------------------------------------------------------------------
import pytest
from common.read_ini import ReadIni


def run_ere():
    # 实例化测试条件对象 用于装测试用例
    # 获取用例路径
    case_path = ReadIni().get_case_path()
    pytest.main(['-vs', case_path + r"ere_case\test_ere_mod.py"])


if __name__ == '__main__':
    run_ere()
