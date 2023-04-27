# =============================================
# 参数化的数据可以是列表套元组的形式[(a,b),(c,d).....]
# 也可以是列表套列表[[a,b],[c,d]...]
# 可以通过excel读取
# 列表中嵌套了多少个元组，就有多少条用例

# =============================================

import pytest
import logging
from process.ere_CFR import ere_cfr_process
from common.get_video_info_to_json import get_video_info_to_json
from time import sleep
from common.read_excel import read_excel

# 配置日志
# logging.basicConfig(level=logging.info)
# logger = logging.getLogger()


# 参数化
@pytest.mark.parametrize("set_fps, time",
                         read_excel(r"E:\python\gitproject\auto_web_GUI\data_config\ere_cfr_case.xlsx", "Sheet1"))
def test_cfr1(set_fps, time):
    """
    固定帧率测试
    :param set_fps: 测试覆盖的帧率
    :param time: 录制时长
    :return:
    """

    ere_cfr_process(set_fps, time)
    sleep(3)
    video_fps = get_video_info_to_json(r"E:\test_material\ere_record")["帧率"]

    assert int(video_fps) == set_fps  # 判断帧率是否固定到指定的参数
    # 打印日志


    sleep(3)
