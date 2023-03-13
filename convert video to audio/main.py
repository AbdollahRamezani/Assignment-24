import time
from moviepy import editor

videos = [["video1.mp4", "audio1.mp3"], ["video2.mp4", "audio2.mp3"], ["video3.mp4", "audio3.mp3"], ["video4.mp4", "audio4.mp3"]]

start=time.time()
def convert(video, audio):

    video = editor.VideoFileClip(video)
    video.audio.write_audiofile(audio)


for video, audio in videos:
    convert(video, audio)
end=time.time()    


print("time : ", end-start)