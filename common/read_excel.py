# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:  game_auto
# FileName:     read_excel
# Author:      xiaoxiao
# Datetime:    2022/8/3 15:21
# -----------------------------------------------------------------------------------
from openpyxl import load_workbook


def read_excel(filename, sheet_name):
    # 打开文件
    wb = load_workbook(filename)
    # 选择sheet页
    ws = wb[sheet_name]
    # 创建一个空列表，用来装所有的用例：
    kong = []
    # 第一个for循环遍历的是一行的数据
    for hang_tuple in ws:
        case = []
        # 第二个for循环遍历的是当个单元格的数据
        for i in hang_tuple:
            # 筛选为空的单元格
            if i.value == None:
                # 重新赋值为空字符串
                i.value = ""
            case.append(i.value)
        kong.append(case)
    print(kong[1::])
    return kong[1::]


if __name__ == '__main__':
    read_excel(r"../data_config/ere_cfr_case.xlsx", "Sheet1")

