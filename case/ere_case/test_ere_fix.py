import pytest
from process.Ere_fix import ere_fix_process
from common.get_video_info_to_json import get_video_info_to_json
from time import sleep
import logging
from common.read_excel import read_excel
import os


# 参数化
@pytest.mark.parametrize("set_fps, time, record_format, gpu",
                         read_excel(r"E:\python\gitproject\auto_web_GUI\data_config\xxx.xlsx", "Sheet1"))
def test_fix(record_format, time):
    ere_fix_process(record_format, time)

    get_video_info_to_json("文件修复地址")

    try:
        assert time == video_time  # 恢复时长、恢复格式、播放正常

    finally:
        pass

