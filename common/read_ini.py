# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pro_ranzhi48
# FileName:     read_ini
# Author:      MingFeiyang
# Datetime:    2022/8/4 10:59
# Description：
# -----------------------------------------------------------------------------------
# 思路：
# 1、自动获取项目在你电脑上的位置
# 2、手动配置文件在项目中的路径
# 3、把第一步和第二步的结果拼接在一起，就能得到完整的路径

import os
from configparser import ConfigParser


class ReadIni:

    def __init__(self):
        self.pro_url = os.path.dirname(__file__).split('common')[0]
        # 实例化对象
        self.config = ConfigParser()
        # 找到ini文件
        self.config.read(self.pro_url + r"\data_config\data_config.ini")

    def get_yaml_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "yaml_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_json_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "json_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_excel_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "excel_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_screenshot_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "screenshot_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_log_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "log_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_report_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "report_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_case_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "case_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_video_js_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "video_js_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)

    def get_video_path(self):
        # 读取ini文件的内容
        file_url = self.config.get("path", "record_video_path")
        # 拼接成完整路径
        return os.path.join(self.pro_url, file_url)


if __name__ == '__main__':
    r = ReadIni()
    print(r.get_yaml_path())
    print(r.get_json_path())
    print(r.get_excel_path())
    print(r.get_video_path())

