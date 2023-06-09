# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : get_video_info_to_json.py
# Time       ：2023/4/24 13:54
# Author     ：Soozi
# version    ：python 3.8
# Description：获取视频基本参数 需要安装ffmpeg-python库（pip install ffmpeg-python）
# 需要下载ffmpeg工具包，配置ffmpeg环境变量
"""
import logging

import ffmpeg
import cv2
from decimal import Decimal
import time
import json
from common.read_ini import ReadIni
from common.log import *


def get_video_info_to_json_with_ffmpeg(source_video_path=r"C:\Users\admini\Downloads"):
    global video_info_dict, packge_format, origin_path

    """遍历目录"""
    path = source_video_path  # 要遍历的目录
    for root, dirs, names in os.walk(path):
        for name in names:
            ext = os.path.splitext(name)[1]  # 获取后缀名
            if ext == '.mp4':
                origin_path = os.path.join(root, name)  # mp4文件原始地址
                packge_format = "MP4"
            elif ext == ".mov":
                origin_path = os.path.join(root, name)  # mp4文件原始地址
                packge_format = "MOV"
            elif ext == ".avi":
                origin_path = os.path.join(root, name)  # mp4文件原始地址
                packge_format = "AVI"

    probe = ffmpeg.probe(origin_path)
    probe_cv2 = cv2.VideoCapture(origin_path)
    print(probe)
    video_path = origin_path
    format = probe['format']
    bit_rate = Decimal(int(format['bit_rate']) / 1000).quantize(Decimal("0.00"))  # 比特率
    duration = Decimal(format['duration']).quantize(Decimal("0.00"))  # 视频时长
    size = Decimal(int(format['size']) / 1024 / 1024).quantize(Decimal("0.00"))  # 视频大小

    """判断是否存在视频流"""
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found')
    else:
        width = int(video_stream['width'])  # 宽
        height = int(video_stream['height'])  # 高
        video_code_name = video_stream["codec_name"]  # 编码格式
        #  帧率
        fps = int(probe_cv2.get(cv2.CAP_PROP_FPS))

        video_info_dict = {"视频路径": str(video_path),
                           "宽": width,
                           "高": height,
                           "视频编码格式": video_code_name,
                           "帧率": fps,
                           "比特率": str(bit_rate),
                           "视频大小": str(size),
                           "视频时长": str(duration),
                           "封装格式": str(packge_format)}

    """判断是否存在音频流"""
    audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
    if audio_stream is None:
        print('No audio stream found')
    else:

        codec_name = audio_stream['codec_name']  # 音频编码格式
        sample_rate = audio_stream['sample_rate']  # 音频采样率
        video_info_dict.update(音频编码格式=codec_name, 音频采样率=sample_rate)

    """将数据写入json文件"""
    test_time = time.strftime("%Y_%m_%d_%H-%M-%S")
    js_name = ReadIni().get_video_js_path() + "video_info_{}.json".format(test_time)  # 获取的视频数据保存的地址
    with open(js_name, "w", encoding='utf-8') as f:
        json.dump(video_info_dict, f, ensure_ascii=False)
    print(video_info_dict)
    return video_info_dict


def get_total_frames_with_cv2(video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not video.isOpened():
        print("无法打开视频文件")
        return

    # 获取视频的信息
    codec = int(video.get(cv2.CAP_PROP_FOURCC))
    bitrate = int(video.get(cv2.CAP_PROP_BITRATE))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    avg_fps = total_frames / duration

    # 关闭视频文件
    video.release()
    print(fps, width, height, codec, bitrate, duration, avg_fps, total_frames)

    return fps


if __name__ == '__main__':
    get_total_frames_with_cv2(r"E:\python\gitproject\auto_web_GUI\record_video\20230512_104842.avi")
