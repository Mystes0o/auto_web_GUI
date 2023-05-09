from time import sleep
import json
import pyautogui
from common.log import *
from common.base_gui import coordinate_click
from common.read_ini import ReadIni


def video_compression():

    os.startfile(r"E:\Program Files\RecExperts\bin\RecExperts.exe")  # 打开ere
    coordinate_click("播放器按钮")   # 点击播放器
