#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
YouTube to TikTok 主入口文件

使用示例：展示如何使用项目功能，包括cookies配置和视频下载。
'''

import os
import sys

# 将项目根目录添加到sys.path中
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from core.youtube_downloader import YouTubeDownloader
from utils.logger import logger


def configure_cookies():
    """
    配置cookies的指导信息
    """
    print("=" * 60)
    print("📝 Cookies配置指导")
    print("=" * 60)
    print("为了解决YouTube的登录验证问题，您需要配置cookies。有两种方式：")
    print()
    print("方式1：使用浏览器cookies（推荐）")
    print("1. 确保您已经在浏览器中登录了YouTube")
    print("2. 在config/settings.py中设置：")
    print("   BROWSER_COOKIES = \"chrome\"  # 或\"firefox\", \"edge\"等")
    print()
    print("方式2：使用cookies文件")
    print("1. 安装浏览器扩展（如Chrome的\"Get cookies.txt LOCALLY\"）")
    print("2. 访问YouTube网站并导出cookies为txt文件")
    print("3. 将cookies.txt文件放在项目根目录")
    print("4. 在config/settings.py中设置：")
    print("   import os")
    print("   COOKIES_FILE = os.path.join(PROJECT_ROOT, \"cookies.txt\")")
    print()
    print("完成配置后，请重新运行此脚本。")
    print("=" * 60)


def main():
    """
    主函数：展示项目使用流程
    """
    logger.info("启动YouTube to TikTok工具")
    
    # 配置cookies检查
    from config.settings import BROWSER_COOKIES, COOKIES_FILE
    if not BROWSER_COOKIES and not COOKIES_FILE:
        configure_cookies()
        return
    
    # 初始化下载器
    downloader = YouTubeDownloader()
    
    # 示例1：下载单个视频
    print("\n🚀 示例1：下载单个YouTube视频")
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # 示例视频链接
    print(f"正在下载视频：{video_url}")
    
    result = downloader.download_video(video_url)
    if result:
        print(f"✅ 下载成功！")
        print(f"   视频路径：{result['video_path']}")
        print(f"   字幕路径：{result['subtitle_paths']}")
    else:
        print(f"❌ 下载失败！")
    
    # 示例2：批量下载视频
    print("\n🚀 示例2：批量下载YouTube视频")
    video_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        # 添加更多视频链接...
    ]
    
    if len(video_urls) > 1:
        results = downloader.batch_download(video_urls)
        print(f"✅ 批量下载完成！")
        print(f"   成功下载：{len(results)}个视频")
    
    print("\n🎉 所有操作完成！")
    logger.info("YouTube to TikTok工具运行结束")


if __name__ == "__main__":
    main()