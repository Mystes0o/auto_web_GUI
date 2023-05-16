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
import pyautogui
from common.log import *
from common.base_gui import coordinate_click
from common.read_ini import ReadIni
from common.ere_config import revise_config
from process import ere_record_gamemod, ere_auto


def ere_cfr_process(mod, set_fps, time, record_format, gpu, camera, microphone, auto_segmentation, auto_stop):  # 录制流程
    """
    :param auto_stop:
    :param auto_segmentation:
    :param microphone:
    :param camera:
    :param virtual_display: 开启虚拟显示器
    :param gpu: 是否开启GPU加速
    :param record_format: 选择视频的录制格式
    :param set_fps: 选择帧数
    :param mod: 录制模式全屏、窗口、游戏
    :param time: 录制的时间长度(s)
    :return: None
    """
    pic_path = ReadIni().get_pic_path()
    revise_config(set_fps, gpu, record_format)  # 修改配置文件
    sleep(1)
    logging.info("打开ere...")
    os.startfile(r"E:\Program Files\RecExperts\bin\RecExperts.exe")  # 打开ere
    sleep(10)

    logging.info("选择录制模式...")
    if mod == 1:  # 全屏
        logging.info("全屏...")
        coordinate_click(pic_path + "full_screen.png")
    elif mod == 2:  # 区域
        logging.info("区域...")
        coordinate_click(pic_path + "partial.png")
        pyautogui.moveTo(1, 1, duration=0.5)
        pyautogui.dragRel(1920, 1080, 1, button='left')
    elif mod == 3:  # 游戏
        logging.info("游戏...")
        ere_record_gamemod.game_mod(1)
    else:
        pass

    if camera == 1:
        logging.info("打开摄像头...")
        coordinate_click(pic_path + "camera.png")

    if microphone == 1:
        logging.info("打开麦克风降噪...")
        coordinate_click(pic_path + "microphone.png")
        coordinate_click(pic_path + "noise_reduction.png")

    if auto_segmentation == 1:
        logging.info("自动分割...")
        ere_auto.auto_segmentation()

    # if virtual_display == 1:
    #     coordinate_click("虚拟显示器打钩")  # 2222222
    #     coordinate_click("OK")  # 点下OK
    # else:
    #     pass

    if auto_stop == 1:
        logging.info("自动停止...")
        ere_auto.auto_stop()

    logging.info("开始录制...")
    try:
        pyautogui.press('f9')  # 按F9开始录制
        sleep(time + 1)
        pyautogui.press('f9')  # 按F9停止录制
        sleep(3)
        os.system("taskkill /f /im RecExperts.exe")  # 强制结束ere
        logging.info("录制结束...")
    except IOError:
        logging.error("录制失败")


if __name__ == '__main__':
    ere_cfr_process(1, 90, 300, "MP4", 'true', 1, 1, 1, 1)
