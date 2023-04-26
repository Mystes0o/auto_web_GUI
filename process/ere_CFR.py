# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ere_CFR.py
# Time       ：2023/4/25 9:59
# Author     ：Soozi
# version    ：python 3.8
# Description：固定帧率的GUI流程
"""

from common import base_gui
from time import sleep
import os
import json


class EreCfrProcess:  # 固定帧率录制流程

    def ere_cfr_process(self, cfr, fps, resolution, mod, time, ):
        """
        :param cfr: 录制模式是否录制固定帧率
        :param fps: 选择帧数
        :param resolution: 分辨率选择
        :param mod: 录制模式全屏、窗口、游戏
        :return:
        """
        # 修改ere配置文件
        with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'r',
                  encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            print(type(load_dict))
            print(load_dict)
            load_dict['video-option']['frame-rate-select'] = fps
        with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
            json.dump(load_dict, load_f, ensure_ascii=False)
            print(type(load_dict))
            print(load_dict)

        os.startfile(r"C:\Program Files (x86)\EaseUS\RecExperts\bin\RecExperts.exe")  # 打开ere
        sleep(5)
        base_gui.coordinate_click(r"../picture/coordinate_pic/share.png")  # 随便点点



if __name__ == '__main__':
    test = EreCfrProcess()
    test.ere_cfr_process()

