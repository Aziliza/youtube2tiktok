# YouTube to TikTok 视频处理工具

一个自动化的Python工具，用于从YouTube下载视频和字幕，翻译配音后上传到TikTok平台。

## 功能特点

- 📥 **YouTube视频下载**：支持批量下载YouTube视频和字幕文件
- 📝 **字幕处理**：自动提取和处理字幕文件
- 🌐 **字幕翻译**：支持多语言字幕翻译（默认英文→中文）
- 🎤 **文本转语音**：将翻译后的字幕转换为语音配音
- 🎬 **视频处理**：视频剪辑、格式转换、画面调整（适配TikTok）
- 📤 **TikTok上传**：自动上传处理后的视频到TikTok平台

## 技术栈

- **Python 3.10+**：项目开发语言
- **yt-dlp**：YouTube视频和字幕下载
- **FFmpeg**：视频和音频处理
- **python-docx**：文档处理（可选）
- **pyttsx3/edge_tts**：文本转语音
- **googletrans**：字幕翻译
- **TikTok API**：TikTok视频上传

## 项目结构

```
youtube2tiktok/
├── config/                # 配置文件目录
│   ├── __init__.py        # 配置导出
│   ├── secrets.py         # 敏感配置（API密钥等）
│   └── settings.py        # 项目设置
├── core/                 # 核心功能模块
│   ├── __init__.py        # 核心功能导出
│   └── youtube_downloader.py  # YouTube下载器
├── data/                 # 数据存储目录
│   ├── audio/            # 音频文件
│   ├── processed_videos/  # 处理后的视频
│   ├── raw_videos/        # 原始下载视频
│   └── subtitles/        # 字幕文件
├── logs/                 # 日志文件目录
├── services/             # 服务模块
│   └── __init__.py        # 服务导出
├── utils/                # 工具函数
│   ├── __init__.py        # 工具导出
│   └── logger.py          # 日志工具
├── .gitignore            # Git忽略文件
├── .python-version       # Python版本管理
├── README.md             # 项目说明文档
├── pyproject.toml        # 项目依赖配置
└── uv.lock               # 依赖锁定文件
```

## 安装方法

1. **克隆项目**

```bash
git clone https://github.com/yourusername/youtube2tiktok.git
cd youtube2tiktok
```

2. **创建虚拟环境**

```bash
# 使用Python内置venv
python -m venv .venv

# 激活虚拟环境
# Windows
.venv\Scripts\activate
# Linux/MacOS
source .venv/bin/activate
```

3. **安装依赖**

```bash
# 使用uv安装依赖
uv install

# 或使用pip
pip install -r requirements.txt
```

4. **配置环境变量**

复制并修改配置文件：

```bash
# 复制配置示例（如果有）
# cp config/secrets.example.py config/secrets.py
```

在`config/settings.py`中配置必要的参数，如API密钥等。

## 使用说明

### 基本用法

```python
from youtube2tiktok import YouTubeDownloader

# 初始化下载器
downloader = YouTubeDownloader()

# 下载单个视频
result = downloader.download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
if result:
    print(f"视频路径: {result['video_path']}")
    print(f"字幕路径: {result['subtitle_paths']}")

# 批量下载视频
urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=another_video_id"
]
results = downloader.batch_download(urls)
for result in results:
    print(f"视频路径: {result['video_path']}")
```

### 完整工作流程

1. **下载视频和字幕**
2. **翻译字幕**（后续实现）
3. **生成配音**（后续实现）
4. **处理视频**（后续实现）
5. **上传到TikTok**（后续实现）

## 配置说明

主要配置文件位于`config/settings.py`，包含以下配置项：

- **路径配置**：视频、音频、字幕等存储路径
- **业务配置**：语言、视频质量、时长限制等
- **字幕配置**：字幕格式、是否下载自动生成字幕等
- **翻译配置**：翻译服务选择
- **配音配置**：TTS服务、语音类型、语速等
- **TikTok配置**：API密钥、视频分类、隐私设置等

## 后续开发计划

- [ ] 实现字幕翻译功能
- [ ] 实现文本转语音配音功能
- [ ] 实现视频处理和剪辑功能
- [ ] 实现TikTok自动上传功能
- [ ] 添加图形用户界面（GUI）
- [ ] 支持更多视频平台

## 贡献指南

欢迎提交Issue和Pull Request！

## 许可证

[MIT License](LICENSE)

## 联系方式

作者: qianyu

---

**注意**：本项目仅供学习和研究使用，请遵守相关平台的使用条款和版权法规。