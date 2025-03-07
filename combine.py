import ffmpeg.exe
import os

def merge_video_and_audio(video_file, audio_file):
    # 提取影片檔案名稱（不包括擴展名）
    base_name = os.path.splitext(video_file)[0]
    output_file = f"{base_name}_merged.mp4"  # 輸出的合併檔案名稱與影片檔案名稱相同
    
    # 使用 ffmpeg 合併影片和音訊
    command = [
        'ffmpeg', 
        '-i', video_file,   # 影片檔案
        '-i', audio_file,   # 音訊檔案
        '-c:v', 'copy',     # 影片流直接複製
        '-c:a', 'aac',      # 將音訊轉為 aac 格式
        '-strict', 'experimental',  # 使用 experimental 音訊編碼
        output_file         # 輸出的合併檔案
    ]
    
    # 執行命令
    
    ffmpeg.run(command)
    os.remove(video_file)
    os.remove(audio_file)
    print(f"合併完成，輸出檔案：{output_file}")

# 提供影片和音訊檔案的路徑
