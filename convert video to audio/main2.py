import time
from moviepy import editor
from threading import Thread

videos = [["video1.mp4", "audio1.mp3"], ["video2.mp4", "audio2.mp3"], ["video3.mp4", "audio3.mp3"], ["video4.mp4", "audio4.mp3"]]

def convert(video, audio):

    video = editor.VideoFileClip(video)
    video.audio.write_audiofile(audio)

start = time.time()
threads = []
for video, audio in videos:
    threads.append(Thread(target=convert, args=[video, audio]))

for t in threads:
    t.start()

for t in threads:
    t.join()
        
end = time.time()
print("time: ", end - start)