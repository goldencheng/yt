from yt_dlp import YoutubeDL
import yt_dlp
import os
from combine import merge_video_and_audio
def download_video(url):
    options = {
        'format': 'bestvideo[height=720]+bestaudio/best[height=720]',  # 明確選擇 720p
        'merge_output_format': 'mp4',  # 合併影片與音訊
        'outtmpl': '%(title)s.%(ext)s',  # 影片檔名（使用影片標題）
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])
        # 返回影片標題（檔案名稱）
        return ydl.prepare_filename(ydl.extract_info(url, download=False))

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio',  # 只下載最佳音質
        'outtmpl': '%(title)s.%(ext)s',  # 音訊檔名
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',  # 提取音訊
            'preferredcodec': 'mp3',  # 轉換為 mp3 格式
            'preferredquality': '192',  # 設定音質為 192kbps
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        # 返回音訊檔案名稱
        return ydl.prepare_filename(ydl.extract_info(url, download=False))

def name(video_file):
    base_name = os.path.splitext(video_file)[0]
    output_file = f"{base_name}"  
    return output_file+"mp4",output_file+"mp3"


video_url = input("請輸入 YouTube 影片網址: ")

# 下載影片和音訊並獲取檔案名稱
video_file = download_video(video_url)
audio_file = download_audio(video_url)
merge_video_and_audio(name(video_file))

print("下載並合併完成！")


