import json
import os
a = 180
b = 120
st = f"{a} + {b} = {a + b}"
print(st)
import cv2
vid = cv2.VideoCapture(r"C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\Установка Python 39 на Linux из исходного кода  Python 39 Install.mp4")
width = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(int(width))
CompressedVideos = {"dddfdffd":[None,"iofiffufryruuyurut","ieroeyr8ur8re8"]}
HomeDir = os.path.dirname(os.path.realpath(__file__))
with open(HomeDir + "/test.json", "w") as outfile:
  json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
for User in CompressedVideos:
  for i,Video in enumerate(CompressedVideos[User]):
    if CompressedVideos[User][i] != None:
      print("Hello world!")
print(CompressedVideos)
#os.chmod(r"C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\Python Django Blog In Less Than 20 Minutes - Blogging website tutorial.mp4", 0o777)
test = {133232232323:["jdfhogoufhgur"],
        44343444:["hrtuhruthrt"],
}
#test[44343444].remove("hrtuhruthrt")
if test[44343444][0]:
  print("Hello world!")
from pytube import YouTube


yt = YouTube('https://youtu.be/YXmsi13cMhw')
streams = yt.streams

video_best = streams.order_by('resolution').desc().first()
video = streams.filter(res = '1080p',only_video=True).desc().first()
video.download(filename = 'test_video.mp4')
audio = streams.filter(only_audio=True).desc().first()
audio.download(filename = 'test_audio.mp4')
os.chdir(HomeDir + "/ffmpeg/bin")
os.system(r'ffmpeg -i "C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\test_video.mp4" -i "C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\test_audio.mp4" -c:v copy -c:a aac "C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\test_output.mp4"')