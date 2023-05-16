import json
from common.read_ini import ReadIni


def revise_config(set_fps, gpu, record_format):
    """
    :param set_fps:
    :param gpu:
    :param record_format:
    :return:
    """
    """修改配置文件"""
    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        # load_dict['video-option']['frame-rate-select'] = cfr
        load_dict['video-option']['frame-rate-select'] = set_fps  # 修改json内容
        # load_dict['video-option']['frame-rate-select'] = resolution
        load_dict['recording-option']['gpu'] = gpu  # GPU加速
        load_dict['video-option']['formats-select'] = record_format  # 录制格式
        load_dict['base-option']['output'] = ReadIni().get_video_path()  # 修改视频保存地址

    with open(r"C:\Users\admini\AppData\Local\EaseUS\EaseUS RecExperts\settings.json", 'w', encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)
