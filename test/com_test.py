
import common.get_video_info_to_json
import os
import time
import pyautogui


def get_mouse_positon():
    time.sleep(5)  # ׼��ʱ��
    print('��ʼ��ȡ���λ��')
    try:
        for i in range(10):
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            positionStr = '�������㣨X,Y��Ϊ��{},{}'.format(str(x).rjust(4), str(y).rjust(4))
            pix = pyautogui.screenshot().getpixel((x, y))  # ��ȡ���������Ļ���RGB��ɫ
            positionStr += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
                3) + ')'
            print(positionStr)
            time.sleep(0.5)  # ͣ��ʱ��
    except:
        print('��ȡ���λ��ʧ��')


if __name__ == "__main__":
    get_mouse_positon()
