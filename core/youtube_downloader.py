import os
import sys
import yt_dlp
from typing import Optional, Dict, Any, List

# 将项目根目录添加到sys.path中，以便正确导入模块
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from config.settings import (
    RAW_VIDEO_DIR,
    VIDEO_QUALITY,
    PROJECT_ROOT,
    SUBTITLE_DIR,
    VIDEO_INFO_DIR,
    AUDIO_DIR,
    SUBTITLE_FORMAT,
    SOURCE_LANGUAGE,
    DOWNLOAD_AUTO_GENERATED_SUBTITLES,
    BROWSER_COOKIES,
    COOKIES_FILE
)
from utils.logger import setup_logger

# 初始化日志
logger = setup_logger("youtube_downloader")

# 确保下载目录存在
os.makedirs(RAW_VIDEO_DIR, exist_ok=True)

class YouTubeDownloader:
    def __init__(self):
        """初始化下载配置，适配TikTok上传要求（MP4格式、720P以内）"""
        # 核心配置项（可根据需求调整）
        self.ydl_opts = {
            # 1. 格式选择：优先选指定清晰度的MP4，音视频合并
            # format说明：bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]
            # 'format': f'bestvideo[height<={VIDEO_QUALITY.split("p")[0]}][ext=mp4]+bestaudio[ext=m4a]/best[height<={VIDEO_QUALITY.split("p")[0]}][ext=mp4]',
            'format': 'bestvideo+bestaudio/best',
            
            # 2. 输出配置：指定目录+统一文件名格式（避免特殊字符）
            'outtmpl': os.path.join(RAW_VIDEO_DIR, '%(title)s_%(id)s.%(ext)s'),
            # 强制合并为MP4（TikTok仅支持MP4/AVI等）
            'merge_output_format': 'mp4',
            
            # 3. 性能/稳定性配置
            'continuedl': True,  # 断点续传
            'retries': 3,  # 下载失败重试次数
            'quiet': False,  # 显示下载进度
            'no_warnings': True,  # 屏蔽无关警告
            'ignoreerrors': False,  # 遇到错误终止（避免无效文件）
            
            # 4. 元数据提取：保存视频信息（标题、时长、封面等）
            'writedescription': False,  # 不下载描述文件（可选开启）
            'writeinfojson': True,  # 保存视频元信息到JSON文件（方便后续用）
            'infojson_outtmpl': os.path.join(VIDEO_INFO_DIR, '%(title)s_%(id)s.info.json'),  # 视频信息JSON保存路径
            'json_download': False,
            
            # 5. 字幕配置
            'writesubtitles': True,  # 下载字幕
            'writeautomaticsub': DOWNLOAD_AUTO_GENERATED_SUBTITLES,  # 下载自动生成的字幕
            'subtitleslangs': [SOURCE_LANGUAGE],  # 下载的字幕语言
            'subtitlesformat': SUBTITLE_FORMAT,  # 字幕格式
            'subtitle_outtmpl': os.path.join(SUBTITLE_DIR, '%(title)s_%(id)s.%(ext)s'),  # 字幕输出路径
            
            # 6. Cookies配置：解决登录验证问题
            'cookiefile': COOKIES_FILE if COOKIES_FILE and os.path.exists(COOKIES_FILE) else None,
            
            # 7. 其他：跳过已下载的视频
            'download_archive': os.path.join(PROJECT_ROOT, 'logs/downloaded_videos.txt'),
        }
        
        # 添加浏览器cookies支持
        if BROWSER_COOKIES:
            # 根据yt-dlp文档，cookiesfrombrowser参数可以是字符串格式"browser[:profile][:container]" 
            # 或者是包含浏览器名称和其他可选参数的列表/元组
            # 这里我们支持两种格式：简单字符串或列表
            if isinstance(BROWSER_COOKIES, str):
                self.ydl_opts['cookiesfrombrowser'] = BROWSER_COOKIES
            elif isinstance(BROWSER_COOKIES, (list, tuple)):
                self.ydl_opts['cookiesfrombrowser'] = BROWSER_COOKIES
            else:
                # 默认处理为字符串
                self.ydl_opts['cookiesfrombrowser'] = str(BROWSER_COOKIES)
            logger.info(f"已配置使用{self.ydl_opts['cookiesfrombrowser']}浏览器的cookies")
        elif self.ydl_opts['cookiefile']:
            logger.info(f"已配置使用cookies文件：{self.ydl_opts['cookiefile']}")
        else:
            logger.warning("未配置cookies，可能无法下载部分需要登录的视频")

    def get_video_info(self, url: str) -> Optional[Dict[str, Any]]:
        """仅提取视频元信息（不下载），用于前置校验"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # 提取信息但不下载
                info = ydl.extract_info(url, download=False)
                logger.info(f"提取视频信息成功：标题={info.get('title')}，时长={info.get('duration')}秒")
                return info
        except Exception as e:
            logger.error(f"提取视频信息失败：{str(e)}", exc_info=True)
            return None

    def download_video(self, url: str) -> Optional[Dict[str, Any]]:
        """
        下载YouTube视频和字幕到指定目录
        :param url: YouTube视频链接（支持普通链接/短链接）
        :return: 包含视频路径和字幕路径的字典，失败返回None
        """
        # 前置校验：先检查链接是否有效
        video_info = self.get_video_info(url)
        if not video_info:
            return None

        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # 执行下载
                ydl.download([url])
                # 获取下载后的文件路径
                video_path = ydl.prepare_filename(video_info)
                # 处理后缀（合并后可能是.mp4，需修正）
                if os.path.exists(video_path.replace('.mkv', '.mp4')):
                    video_path = video_path.replace('.mkv', '.mp4')
                
                # 获取字幕文件路径
                subtitle_paths = []
                title = video_info.get('title')
                video_id = video_info.get('id')
                
                # 检查各种可能的字幕文件路径
                possible_subtitle_paths = [
                    os.path.join(SUBTITLE_DIR, f"{title}_{video_id}.{SUBTITLE_FORMAT}"),
                    os.path.join(RAW_VIDEO_DIR, f"{title}_{video_id}.{SOURCE_LANGUAGE}.{SUBTITLE_FORMAT}"),
                    os.path.join(RAW_VIDEO_DIR, f"{title}_{video_id}.{SUBTITLE_FORMAT}")
                ]
                
                for path in possible_subtitle_paths:
                    if os.path.exists(path):
                        subtitle_paths.append(path)
                
                logger.info(f"视频下载完成：{video_path}")
                if subtitle_paths:
                    logger.info(f"字幕下载完成：{subtitle_paths}")
                else:
                    logger.warning(f"未找到字幕文件")
                
                return {
                    'video_path': video_path,
                    'subtitle_paths': subtitle_paths,
                    'video_info': video_info
                }
        except Exception as e:
            logger.error(f"下载视频失败：{str(e)}", exc_info=True)
            return None

    def batch_download(self, url_list: list) -> list:
        """批量下载多个视频和字幕"""
        success_results = []
        for idx, url in enumerate(url_list):
            logger.info(f"开始下载第{idx+1}/{len(url_list)}个视频：{url}")
            result = self.download_video(url)
            if result:
                success_results.append(result)
        logger.info(f"批量下载完成：成功{len(success_results)}/{len(url_list)}个")
        return success_results

# 测试用例（可在main.py中调用）
if __name__ == "__main__":
    downloader = YouTubeDownloader()
    # 单视频下载示例
    test_url = "https://www.youtube.com/shorts/U9vZjYmt81c"
    result = downloader.download_video(test_url)
    if result:
        print(f"测试下载成功：")
        print(f"视频路径：{result['video_path']}")
        print(f"字幕路径：{result['subtitle_paths']}")