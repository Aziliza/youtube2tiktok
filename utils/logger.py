'''
Author: qianyu
Date: 2026-01-20 15:16:57
LastEditTime: 2026-01-20 15:17:10
'''
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

# 将项目根目录添加到sys.path中，以便正确导入模块
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from config.settings import PROJECT_ROOT

# 定义日志目录（放在项目根目录的 logs 文件夹）
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
# 确保日志目录存在
os.makedirs(LOG_DIR, exist_ok=True)

# 日志格式配置
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
# 时间格式
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def setup_logger(
    logger_name: str = "youtube2tiktok",
    log_level: int = logging.INFO,
    log_file_prefix: str = "app"
) -> logging.Logger:
    """
    初始化并返回一个配置好的 logger 实例
    :param logger_name: logger 名称（用于区分不同模块的日志）
    :param log_level: 日志级别（默认 INFO，调试时可设为 DEBUG）
    :param log_file_prefix: 日志文件前缀（生成的文件如 app_2026-01-20.log）
    :return: 配置好的 Logger 对象
    """
    # 1. 创建 logger 实例，避免重复添加处理器
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    # 清空已有的处理器（防止重复输出）
    if logger.handlers:
        logger.handlers.clear()

    # 2. 创建控制台处理器（输出到终端）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    console_handler.setFormatter(console_formatter)

    # 3. 创建文件处理器（按日期分割，保留7天日志）
    log_file_path = os.path.join(LOG_DIR, f"{log_file_prefix}.log")
    # TimedRotatingFileHandler 参数说明：
    # when="D"：按天分割；interval=1：每天一个文件；backupCount=7：保留7天日志
    file_handler = TimedRotatingFileHandler(
        filename=log_file_path,
        when="D",
        interval=1,
        backupCount=7,
        encoding="utf-8"  # 确保中文日志不乱码
    )
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_formatter)

    # 4. 给 logger 添加处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# 全局默认 logger（项目中大部分地方可直接用这个）
logger = setup_logger()

# 测试用例
if __name__ == "__main__":
    # 测试不同级别的日志输出
    logger.debug("这是调试信息（仅调试时显示）")
    logger.info("这是普通信息（比如视频下载完成）")
    logger.warning("这是警告信息（比如文件已存在）")
    logger.error("这是错误信息（比如下载失败）")
    
    # 测试模块专属 logger
    downloader_logger = setup_logger("youtube_downloader", logging.DEBUG)
    downloader_logger.debug("下载器初始化完成")