import os
from common.base_gui import coordinate_click
from common.read_ini import ReadIni
import pyautogui
from time import sleep


def game_mod(windows):
    os.startfile(r"E:\Program Files\RecExperts\bin\RecExperts.exe")  # 打开ere
    pic_path = ReadIni().get_pic_path()
    sleep(5)
    coordinate_click(pic_path + "game_mod.png")  # 游戏模式
    sleep(2)
    coordinate_click(pic_path + "choose_game.png")
    if windows == 1:  # 窗口模式流程
        sleep(1)
        pyautogui.moveRel(0, 300, duration=0.25)  # 向下移动50个像素
        pyautogui.click()
        sleep(1)
        coordinate_click(pic_path + "confirm.png")  # 确认
        sleep(1)
    else:  # 进程模式流程
        sleep(1)
        coordinate_click(pic_path + "game_process.png")
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.click()
        sleep(1)
        coordinate_click(pic_path + "confirm.png")  # 确认
        sleep(1)


if __name__ == '__main__':
    game_mod(10)


