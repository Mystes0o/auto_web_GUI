# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : base_gui.py
# Time       ：2023/4/25 10:52
# Author     ：Soozi
# version    ：python 3.8
# Description：  将opencv图像识别和pyautogui，实现软件元素定位和点击
"""
import cv2
import pyautogui


def get_coordinate(img_model_path="None"):
    """
    用来判定屏幕画面的点击坐标
    :param img_model_path:用来检测的图片
    :return:以元组形式返回检测到的区域中心的坐标
    """
    # 将图片截图并且保存
    pyautogui.screenshot().save(r"../picture/ere_auto_pic/screenshot.png")  # 待读取图像
    img = cv2.imread(r"../picture/ere_auto_pic/screenshot.png")  # 图像模板
    img_terminal = cv2.imread(img_model_path)
    height, width, channel = img_terminal.shape  # 读取模板的高度宽度和通道数
    result = cv2.matchTemplate(img, img_terminal, cv2.TM_SQDIFF_NORMED)  # 使用matchTemplate进行模板匹配（标准平方差匹配）
    upper_left = cv2.minMaxLoc(result)[2]    # 解析出匹配区域的左上角图标
    lower_right = (upper_left[0] + width, upper_left[1] + height)   # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
    avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))  # 计算坐标的平均值并将其返回
    return avg


def coordinate_click(path):
    """
    path:需要点击的图像路径
    点击坐标
    """
    coordinate = get_coordinate(path)
    pyautogui.click(coordinate[0], coordinate[1], button="left")  # 左键点击


def input_parameter():

    pass
