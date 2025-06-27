import moviepy as mp
video = mp.VideoFileClip("1号女嘉宾.mp4")
audio = mp.AudioFileClip("1号女嘉宾.mp3")
video.audio = audio
video.write_videofile("video_audio.mp4")