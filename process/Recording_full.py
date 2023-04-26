# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Recording_full.py
# Time       ：2023/4/14 13:12
# Author     ：Soozi
# version    ：python 3.10
# Description：下面是整个视频录制的流程，需要引入pytest测试这个流程
"""
from time import sleep
from common.base_web import Base
from common.base_gui import coordinate_click
import common.get_video_info_to_json
import pyautogui


class RecordPage(Base):
    def recording_video(self, time=10):
        self.click("i", "recording_start")  # 点击开始录制按钮
        self.click("i", "recordingVideoBox")  # 点击打开摄像头
        self.click("i", "recordingMicrophoneBox")  # 点击打开麦克风
        sleep(1)
        coordinate_click(r"../picture/coordinate_pic/allow.png")  # 停顿一秒再截屏，等待网页刷新
        sleep(1)
        coordinate_click(r"../picture/coordinate_pic/allow.png")   # 点击允许三次间隔一秒
        sleep(1)
        coordinate_click(r"../picture/coordinate_pic/allow.png")
        sleep(1)
        self.click("i", "recordingRecorder")  # 点击录制
        sleep(1)
        coordinate_click(r"../picture/coordinate_pic/full_screen.png")  # 使用左键点击坐标
        #  重复上面的过程
        coordinate_click(r"../picture/coordinate_pic/share_system_voice.png")  # 点击分享音频
        pyautogui.moveRel(0, -200, duration=0.25)  # 鼠标向上移动2百个像素点击
        pyautogui.click()
        coordinate_click(r"../picture/coordinate_pic/share1.png")  # 点击share的坐标

        sleep(time + 3)  # 录制多少秒左右,有3秒倒计时
        self.click("i", "recorderStop")
        self.click("i", "recorderSave")  # 下载视频
        sleep(3)
        common.get_video_info_to_json.get_video_info_to_json()  # 获取视频数据保存为json
        sleep(5)


if __name__ == '__main__':
    test = RecordPage("c", url="https://recorder.easeus.com/online-screen-recorder.html")
    test.recording_video(10)
