# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ere_record_mod.py
# Time       ：2023/4/25 9:59
# Author     ：Soozi
# version    ：python 3.8
# Description：固定帧率的GUI流程
"""

from time import sleep
import json
import pyautogui
from common.log import *
from common.base_gui import coordinate_click
from common.read_ini import ReadIni


def ere_cfr_process(set_fps, time, record_format, gpu, virtual_display):  # 录制流程
    """
    :param virtual_display: 开启虚拟显示器
    :param gpu: 是否开启GPU加速
    :param record_format: 选择视频的录制格式
    :param set_fps: 选择帧数
    :param cfr: 录制模式是否录制固定帧率
    :param resolution: 分辨率选择
    :param mod: 录制模式全屏、窗口、游戏
    :param time: 录制的时间长度(s)
    :return:
    """
    """修改配置文件选择录制模式"""
    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        # load_dict['video-option']['frame-rate-select'] = cfr
        load_dict['video-option']['frame-rate-select'] = set_fps  # 修改json内容
        # load_dict['video-option']['frame-rate-select'] = resolution
        load_dict['recording-option']['gpu'] = gpu  # GPU加速
        load_dict['video-option']['formats-select'] = record_format  # 录制格式
        load_dict['base-option']['output'] = ReadIni().get_video_path()  # 修改视频保存地址

    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)
    logging.info("打开ere...")
    os.startfile(r"E:\Program Files\RecExperts\bin\RecExperts.exe")  # 打开ere
    sleep(5)

    """虚拟显示器"""
    if virtual_display == "true":
        coordinate_click("虚拟显示器打钩")  #
        coordinate_click("OK")  # 点下OK
    else:
        pass

    """录制流程"""
    pyautogui.press('f9')  # 按F9开始录制
    sleep(time+6)
    pyautogui.press('f9')  # 按F9停止录制
    sleep(3)
    os.system("taskkill /f /im RecExperts.exe")  # 强制结束ere


if __name__ == '__main__':
    ere_cfr_process(90, 30, "MP4", 'true', "false")
