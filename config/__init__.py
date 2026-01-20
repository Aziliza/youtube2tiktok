'''
Author: qianyu
Date: 2026-01-20 15:14:44
LastEditTime: 2026-01-20 15:28:03
'''
from .settings import (
    # 路径配置
    PROJECT_ROOT,
    RAW_VIDEO_DIR,
    PROCESSED_VIDEO_DIR,
    AUDIO_DIR,
    SUBTITLE_DIR,
    LOG_DIR,
    
    # 业务配置
    SOURCE_LANGUAGE,
    TARGET_LANGUAGE,
    VIDEO_QUALITY,
    MAX_VIDEO_DURATION,
    
    # 字幕配置
    SUBTITLE_FORMAT,
    DOWNLOAD_AUTO_GENERATED_SUBTITLES,
    
    # 翻译配置
    TRANSLATION_SERVICE,
    
    # 配音配置
    TTS_SERVICE,
    TTS_VOICE,
    TTS_RATE,
    TTS_VOLUME,
    
    # TikTok配置
    TIKTOK_APP_KEY,
    TIKTOK_APP_SECRET,
    TIKTOK_ACCESS_TOKEN,
    TIKTOK_CATEGORY,
    TIKTOK_PRIVACY,
    TIKTOK_VIDEO_TYPE,
    
    # Cookies配置
    BROWSER_COOKIES,
    COOKIES_FILE,
)