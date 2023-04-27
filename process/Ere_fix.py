# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Ere_fix.py
# Time       ：2023/4/25 10:00
# Author     ：Soozi
# version    ：python 3.8
# Description： 视频修复模块的流程
"""

from time import sleep
import os
import json
import pyautogui


def ere_fix_process(format, time):  # 视频修复流程
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
        # load_dict['video-option']['frame-rate-select'] = set_fps  # 修改json内容
        # load_dict['video-option']['frame-rate-select'] = resolution
        # load_dict['video-option']['frame-rate-select'] = mod
        load_dict['video-option']['formats-select'] = format
    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)
        print(type(load_dict))
        print(load_dict)

    os.startfile(r"C:\Program Files (x86)\EaseUS\RecExperts\bin\RecExperts.exe")  # 打开ere
    sleep(5)
    pyautogui.press('f9')  # 按F9开始录制
    sleep(time+6)
    os.system("taskkill /f /im RecExperts.exe")  # 强制结束ere
    sleep(3)


if __name__ == '__main__':
    ere_fix_process("MP4", 30)



