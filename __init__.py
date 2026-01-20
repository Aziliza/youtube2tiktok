'''YouTube to TikTok 视频处理项目

这是一个从YouTube下载视频和字幕，翻译配音后上传到TikTok的自动化工具。

主要功能包括：
- YouTube视频和字幕下载
- 字幕翻译
- 文本转语音配音
- 视频剪辑和处理
- TikTok视频上传

作者: qianyu
日期: 2026-01-20
版本: 1.0.0
'''

# 版本信息
__version__ = "1.0.0"
__author__ = "qianyu"
__email__ = ""  # 可添加邮箱
__description__ = "YouTube视频下载、翻译配音并上传到TikTok的自动化工具"

# 导出核心功能
from .core.youtube_downloader import YouTubeDownloader

# 导出配置
from .config import *

# 导出工具
from .utils.logger import logger, setup_logger

# 导出服务
# from .services import *  # 后续实现服务层后启用