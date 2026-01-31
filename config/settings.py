'''
Author: qianyu
Date: 2026-01-20 15:14:50
LastEditTime: 2026-01-31 20:16:29
'''

import os

# 路径配置
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_VIDEO_DIR = os.path.join(PROJECT_ROOT, "data/raw_videos")
PROCESSED_VIDEO_DIR = os.path.join(PROJECT_ROOT, "data/processed_videos")
AUDIO_DIR = os.path.join(PROJECT_ROOT, "data/audio")
SUBTITLE_DIR = os.path.join(PROJECT_ROOT, "data/subtitles")

LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# 业务配置
SOURCE_LANGUAGE = "en"  # YouTube视频原始语言
TARGET_LANGUAGE = "zh"  # 目标翻译语言（中文）
VIDEO_QUALITY = "1440p"  # 下载视频质量
MAX_VIDEO_DURATION = 60 * 5  # 最大视频时长（秒），TikTok建议15-60秒，这里设为5分钟

# 字幕配置
SUBTITLE_FORMAT = "srt"  # 字幕格式
DOWNLOAD_AUTO_GENERATED_SUBTITLES = True  # 是否下载自动生成的字幕

# 翻译配置
TRANSLATION_SERVICE = "google"  # 翻译服务：google, baidu, openai等

# 配音配置
TTS_SERVICE = "pyttsx3"  # 文本转语音服务：pyttsx3, edge_tts, openai等
TTS_VOICE = "zh-CN-XiaoxiaoNeural"  # 语音类型
TTS_RATE = 150  # 语速
TTS_VOLUME = 1.0  # 音量

# TikTok配置
TIKTOK_APP_KEY = ""  # TikTok API App Key
TIKTOK_APP_SECRET = ""  # TikTok API App Secret
TIKTOK_ACCESS_TOKEN = ""  # TikTok API Access Token
TIKTOK_CATEGORY = "entertainment"  # TikTok视频分类
TIKTOK_PRIVACY = "public"  # TikTok视频隐私设置：public, private, friends
TIKTOK_VIDEO_TYPE = "vertical"  # TikTok视频类型：vertical(9:16), square(1:1), horizontal(16:9)

# Cookies配置
# 使用浏览器cookies：可以是字符串格式"chrome"或列表格式["chrome", "Default"]
# 如果为None，则不使用浏览器cookies
BROWSER_COOKIES = None  # 例如："chrome" 或 ["chrome", "Default"]
# 或者使用cookies文件路径
COOKIES_FILE = os.path.join(PROJECT_ROOT, "config/cookies.txt")  # 例如：os.path.join(PROJECT_ROOT, "cookies.txt")

# 创建所有必要的目录
for directory in [RAW_VIDEO_DIR, PROCESSED_VIDEO_DIR, AUDIO_DIR, SUBTITLE_DIR, LOG_DIR]:
    os.makedirs(directory, exist_ok=True)