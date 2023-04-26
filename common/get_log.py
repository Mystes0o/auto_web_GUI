# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:
# FileName:     get_log
# Author:      MingFeiyang
# Datetime:    2022/8/4 15:42
# Description：打印测试日志文件
# -----------------------------------------------------------------------------------


import logging


def get_log(filename):
    # 实例化对象
    log = logging.Logger("ezus_online_recorder")
    # 设置日志格式
    formatter = logging.Formatter("[%(asctime)s][%(filename)s][%(levelname)s]:%(message)s")

    # 引用第二个类来进行日志信息处理
    fh = logging.FileHandler(filename, encoding="utf8")
    # 引用上面设置好的日志格式，来规范日志
    fh.setFormatter(formatter)
    # 最后把设置好日志格式日志添加到日志中log中
    log.addHandler(fh)

    # 把最终结果返回给调用者
    return log
