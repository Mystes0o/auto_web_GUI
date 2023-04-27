# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ere_CFR.py
# Time       ：2023/4/25 9:59
# Author     ：Soozi
# version    ：python 3.8
# Description：固定帧率的GUI流程
"""

from time import sleep
import os
import json
import pyautogui


def ere_cfr_process(set_fps, time):  # 固定帧率流程
    """
    :param set_fps: 选择帧数
    :param cfr: 录制模式是否录制固定帧率
    :param resolution: 分辨率选择
    :param mod: 录制模式全屏、窗口、游戏
    :param time: 录制的时间长度
    :return:
    """
    # 修改ere配置文件
    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        print(type(load_dict))
        print(load_dict)
        # load_dict['video-option']['frame-rate-select'] = cfr
        load_dict['video-option']['frame-rate-select'] = set_fps  # 修改json内容
        # load_dict['video-option']['frame-rate-select'] = resolution
        # load_dict['video-option']['frame-rate-select'] = mod
        # load_dict['video-option']['frame-rate-select'] = time

    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)
        print(type(load_dict))
        print(load_dict)

    os.startfile(r"C:\Program Files (x86)\EaseUS\RecExperts\bin\RecExperts.exe")  # 打开ere
    sleep(5)
    pyautogui.press('f9')  # 按F9开始录制
    sleep(time+6)
    pyautogui.press('f9')  # 按F9停止录制
    sleep(3)
    os.system("taskkill /f /im RecExperts.exe")  # 强制结束ere


if __name__ == '__main__':
    ere_cfr_process(90, 30)

