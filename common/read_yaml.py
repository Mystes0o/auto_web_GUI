# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:
# FileName:     read_yaml
# Author:      MingFeiyang
# Datetime:    2022/8/3 16:47
# Description：读取yaml
# -----------------------------------------------------------------------------------


import yaml


def read_yaml(filename):
    with open(filename, mode="r", encoding="utf8") as yaml_data:
        return yaml.safe_load(yaml_data)


if __name__ == '__main__':
    print(read_yaml(r""))
