# =============================================
# 参数化的数据可以是列表套元组的形式[(a,b),(c,d).....]
# 也可以是列表套列表[[a,b],[c,d]...]
# 可以通过excel读取
# 列表中嵌套了多少个元组，就有多少条用例

# =============================================

import pytest
from process.ere_record_mod import ere_cfr_process
from common.get_video_info_to_json import get_video_info_to_json
from time import sleep
from common.log import *
from common.read_excel import read_excel
from common.read_ini import ReadIni


# 参数化
@pytest.mark.parametrize("set_fps, time, record_format, gpu, virtual_display",
                         read_excel(ReadIni().get_excel_path(), "Sheet1"))
def test_cfr1(set_fps, time, record_format, gpu, virtual_display):
    ere_cfr_process(set_fps, time, record_format, gpu, virtual_display)
    sleep(3)
    video_info = get_video_info_to_json(ReadIni().get_video_path())
    logging.info("比对帧数")
    # assert int(video_info["帧率"]) == set_fps  # 判断帧率是否固定到指定的参数
    assert video_info["封装格式"] == record_format  #

    # try:
    #     assert int(video_fps["帧率"]) == set_fps  # 判断帧率是否固定到指定的参数
    #     assert record_format in video_fps  #
    # except:
    #     AssertionError("")
    # finally:
    #     pass


