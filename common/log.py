import logging
import os
from common.read_ini import ReadIni


# 配置日志
log_path = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # 输出到控制台
        logging.FileHandler(os.path.join(log_path, ReadIni().get_log_path() + 'test.log'))  # 输出到文件
    ]
)
