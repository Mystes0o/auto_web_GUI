# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:
# FileName:     read_json
# Author:      MingFeiyang
# Datetime:    2022/8/3 17:04
# Description：读取js
# -----------------------------------------------------------------------------------


import json


def read_json(filename):
    with open(filename, mode="r", encoding="utf8") as json_data:
        return json.load(json_data)

