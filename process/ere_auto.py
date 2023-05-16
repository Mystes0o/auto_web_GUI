# -*- coding: utf-8 -*-

from common.base_gui import coordinate_click
from common.read_ini import ReadIni

pic_path = ReadIni().get_pic_path()


def auto_segmentation():
    coordinate_click(pic_path + "auto_segmentation.png")
    coordinate_click(pic_path + "turn_off_3.png")  # 点击打开
    coordinate_click(pic_path + "confirm.png")


def auto_stop():
    coordinate_click(pic_path + "auto_stop.png")
    coordinate_click(pic_path + "turn_off_3.png")  # 点击打开
    coordinate_click(pic_path + "file_mod.png")
    coordinate_click(pic_path + "confirm.png")
