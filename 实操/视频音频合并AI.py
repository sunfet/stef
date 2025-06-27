import moviepy.editor as mp
import os

# 检查文件是否存在
video_path = '1号女嘉宾.MP4'
audio_path = '1号女嘉宾.MP3'

if not os.path.exists(video_path):
    print(f"错误：视频文件 {video_path} 不存在！")
    exit()

if not os.path.exists(audio_path):
    print(f"错误：音频文件 {audio_path} 不存在！")
    exit()

try:
    # 加载素材
    print("正在加载视频文件...")
    video = mp.VideoFileClip(video_path)
    print("正在加载音频文件...")
    audio = mp.AudioFileClip(audio_path)

    # 剪辑 1,把视频和音频合起来 2. 给视频添加背景音乐 3.给音频加视频
    print("正在合并视频和音频...")
    video = video.set_audio(audio)

    # 导出成品
    print("正在导出视频文件...")
    video.write_videofile('2号女嘉宾.mp4')
    
    # 清理资源
    video.close()
    audio.close()
    print("处理完成！")
    
except Exception as e:
    print(f"发生错误：{str(e)}")