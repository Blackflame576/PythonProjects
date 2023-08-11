#Libreries
from fileinput import filename
import os
from queue import Full
import sys
import threading
import json
import time
import  subprocess
from loguru import logger
import cv2
import platform
import Bot
from pytube import YouTube

#Variables
HomeDir = os.path.dirname(os.path.realpath(__file__))
VideosForCompress = {}
CompressedVideos = {}
HDVideos = {}
FullHDVideos = {}
logger.add(HomeDir + '/DownloadYoutubeBot.log',format="{time} {level} {message}",level="DEBUG",rotation="200 MB",diagnose=True)
isCompress = False
isDownload = False
#Code
#Start function 
def StartUpdateLists():
    while True:
        Bot.StartUploadVideo()

def StartBot():
    PathBotScript = HomeDir + "/Bot.py"
    if platform.system() == "Windows":
        command = f'python {PathBotScript}'
    elif platform.system() == "Linux":
        command = f'python3 {PathBotScript}'
    process = subprocess.Popen(command,shell = True)
    process.wait()

def WriteJson(array,filename):
    outfile = open(HomeDir + f"/{filename}",encoding='UTF-8',mode = "w")
    json.dump(array,outfile,ensure_ascii=False,sort_keys=True, indent=2)

def DownloadVideoHD(TimeForSleep):
    global VideosForCompress
    global CompressedVideos
    global HDVideos
    global FullHDVideos

    if not os.path.exists(HomeDir + '/DownloadVideoHD.json'):
        with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(HDVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/VideosForCompress.json'):
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(VideosForCompress,outfile,ensure_ascii=False,sort_keys=True, indent=2)

    try:
        while isDownload:
            time.sleep(TimeForSleep)
            PathVideo = HomeDir + "/DownloadedVideos"
            i = 0 
            with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "r+") as content:
                HDVideos = json.load(content)
            for User in HDVideos:
                if len(HDVideos[User]) >= 1:
                    for link in HDVideos[User]: 
                        link = link
                        User = User
                        if HDVideos[User][i]:
                            HDVideos[User].remove(link) 
                            with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "w") as outfile:
                                json.dump(HDVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
                            i += 1
                        youtube = YouTube(link)
                        #Settings download audio and video
                        video = youtube.streams.filter(res="1080p",file_extension='mp4',only_video=True).first()
                        audio = youtube.streams.filter(only_audio=True).first()

                        new_name_video = (video.default_filename).replace(".mp4","") + "_video.mp4"
                        new_name_audio = (video.default_filename).replace(".mp4","") + "_audio.mp4"
                        new_path_video = PathVideo + f'/{new_name_video}'
                        new_path_audio = PathVideo + f'/{new_name_audio}'
                        #Download video and audio
                        video.download(PathVideo,filename = new_name_video)
                        audio.download(PathVideo,filename = new_name_audio)
                        logger.info(f"Video '{video.default_filename}' was downloaded.")
                        download = PathVideo + f'/{video.default_filename}'
                        #Merge audio and video to one file MP4
                        process = subprocess.Popen(f'ffmpeg -i "{new_path_video}" -i "{new_path_audio}" -c:v copy -c:a aac "{download}"',shell = True)
                        process.wait()
                        logger.info(f"Audio and video '{video.default_filename}' was merged to one file MP4.")
                        #Remove audio and video for merge to file MP4
                        if os.path.exists(new_path_audio):
                            if platform.system() == "Windows":
                                os.chmod(new_path_audio, 0o777)
                            # os.chmod(Video, os.stat.S_IWRITE)
                            os.remove(new_path_audio)
                        if os.path.exists(new_path_video):
                            if platform.system() == "Windows":
                                os.chmod(new_path_video, 0o777)
                            # os.chmod(Video, os.stat.S_IWRITE)
                            os.remove(new_path_video)
                        #Exists user in list VideosForCompress
                        if User in VideosForCompress:
                            if not download in VideosForCompress[User]:
                                VideosForCompress[User].append(download)
                        elif not User in VideosForCompress:
                            VideosForCompress.update({User:[download]})
                        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
                            json.dump(VideosForCompress, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    except FileNotFoundError:
        with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(HDVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
        with open(HomeDir + "/VideosForCompress.json", "w+") as outfile:
            json.dump(VideosForCompress, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    except json.decoder.JSONDecodeError:
        print("Not have files for download.")
    except IndexError:
        pass

def DownloadVideoFullHD(TimeForSleep):
    global VideosForCompress
    global CompressedVideos
    global HDVideos
    global FullHDVideos

    if not os.path.exists(HomeDir + '/DownloadVideoFullHD.json'):
        with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(FullHDVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/VideosForCompress.json'):
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(VideosForCompress,outfile,ensure_ascii=False,sort_keys=True, indent=2)

    try:
        while isDownload:
            time.sleep(TimeForSleep)
            PathVideo = HomeDir + "/DownloadedVideos"
            i = 0
            with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "r+") as content:
                FullHDVideos = json.load(content)
            for User in FullHDVideos:
                if len(FullHDVideos[User]) >= 1:
                    for link in FullHDVideos[User]: 
                        link = link
                        User = User 
                        if FullHDVideos[User][i]:
                            FullHDVideos[User].remove(link) 
                            with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "w") as outfile:
                                # TempFullHDVideos = json.load(outfile)
                                # TempFullHDVideos[User].remove(link)
                                json.dump(FullHDVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
                            i += 1
                        youtube = YouTube(link)
                        #Settings download audio and video
                        video = youtube.streams.filter(res="1080p",file_extension='mp4',only_video=True).first()
                        audio = youtube.streams.filter(only_audio=True).first()

                        new_name_video = (video.default_filename).replace(".mp4","") + "_video.mp4"
                        new_name_audio = (video.default_filename).replace(".mp4","") + "_audio.mp4"
                        new_path_video = PathVideo + f'/{new_name_video}'
                        new_path_audio = PathVideo + f'/{new_name_audio}'
                        #Download video and audio
                        video.download(PathVideo,filename = new_name_video)
                        audio.download(PathVideo,filename = new_name_audio)
                        logger.info(f"Video '{video.default_filename}' was downloaded.")
                        download = PathVideo + f'/{video.default_filename}'
                        #Merge audio and video to one file MP4
                        process = subprocess.Popen(f'ffmpeg -i "{new_path_video}" -i "{new_path_audio}" -c:v copy -c:a aac "{download}"',shell = True)
                        process.wait()
                        logger.info(f"Audio and video '{video.default_filename}' was merged to one file MP4.")
                        #Remove audio and video for merge to file MP4
                        if os.path.exists(new_path_audio):
                            if platform.system() == "Windows":
                                os.chmod(new_path_audio, 0o777)
                            # os.chmod(Video, os.stat.S_IWRITE)
                            os.remove(new_path_audio)
                        if os.path.exists(new_path_video):
                            if platform.system() == "Windows":
                                os.chmod(new_path_video, 0o777)
                            # os.chmod(Video, os.stat.S_IWRITE)
                            os.remove(new_path_video)
                        #Exists user in list VideosForCompress
                        if User in VideosForCompress:
                            if not download in VideosForCompress[User]:
                                VideosForCompress[User].append(download)
                        elif not User in VideosForCompress:
                            VideosForCompress.update({User:[download]})
                        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
                            json.dump(VideosForCompress, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    except FileNotFoundError:
        with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(FullHDVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
        with open(HomeDir + "/VideosForCompress.json", "w+") as outfile:
            json.dump(VideosForCompress, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    except json.decoder.JSONDecodeError:
        print("Not have files for download.")
    except IndexError:
        pass
def CompressVideo(TimeForSleep):
    global PathVideo
    global VideosForCompress
    global CompressedVideos
    global isCompress
    global User
    global PathNewVideo

    if not os.path.exists(HomeDir + '/VideosForCompress.json'):
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(VideosForCompress,outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/CompressedVideos.json'):
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    
    try:
        while isCompress:
            time.sleep(TimeForSleep)
            with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "r+") as content:
                VideosForCompress = json.load(content)
            i = 0
            for User in VideosForCompress:
                if len(VideosForCompress[User]) >= 1:
                    for Video in VideosForCompress[User]:
                        PathVideo = Video
                        User = User 
                        if VideosForCompress[User][i]:
                            VideosForCompress[User].remove(Video) 
                            with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
                                json.dump(CompressedVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
                            i += 1
                        filename = (os.path.basename(PathVideo)).replace(".mp4","")
                        vid = cv2.VideoCapture(PathVideo)
                        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        print(height)
                        if height <= 720:
                            PathNewVideo = HomeDir + "/Videos/{}_HD_output.mp4".format(filename)
                        elif height == 1080 or height == 960:
                            PathNewVideo = HomeDir + "/Videos/{}_FullHD_output.mp4".format(filename)
                        logger.info(height)
                        #command = f'ffmpeg -i "{PathVideo}"  -codec:a copy -vcodec libx264  -preset fast -crf 32  "{PathNewVideo}"'
                        process = subprocess.Popen(f'ffmpeg -i "{PathVideo}"  -codec:a copy -vcodec libx264  -preset fast -crf 32  "{PathNewVideo}"',shell = True)
                        process.wait()
                        logger.info(f"Video '{filename.replace('.mp4','')}' was compressed.")
                        if User in CompressedVideos:
                            if not PathNewVideo in CompressedVideos[User]:
                                CompressedVideos[User].append(PathNewVideo)
                        elif not User in CompressedVideos:
                            CompressedVideos.update({User:[PathNewVideo]})
                        with open(HomeDir + "/CompressedVideos.json", "w+") as outfile:
                            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
                        logger.info(f"Video '{filename.replace('.mp4','')}' was added to JSON file.")
    except FileNotFoundError:
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(VideosForCompress,outfile,ensure_ascii=False,sort_keys=True, indent=2)
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode="w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
            # output = str(process.communicate())
            # output = output.split("\n")
            # output = output[0].split('\\')
    except json.decoder.JSONDecodeError:
        print("Not have files for compress.")
    # while True:
    #     print("World")
    #     time.sleep(2)
    #os.system(r'ffmpeg -i "C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\Установка Python 39 на Linux из исходного кода  Python 39 Install.mp4"  -codec:a copy -vcodec libx264  -preset fast -crf 32  "C:\Users\Blackflame\Documents\Blackflame\TelegramBots\DownloadYoutubeBot\Videos\output.mp4"')
if __name__ == "__main__":
    if platform.system() == "Windows":
        os.chdir(HomeDir + "/ffmpeg/bin")
    isCompress = True
    th = threading.Thread(target=StartBot, args=())
    th.start()
    logger.info("Thread with Bot.py was started.")
    for i in range(10):
        th = threading.Thread(target=CompressVideo, args=(i,))
        th.start()
        logger.info(f"Thread number {i} with function compress video  was started. ")
    th = threading.Thread(target=StartUpdateLists, args=())
    th.start()
    logger.info("Thread with UpdateLists was started.")
    isDownload = True
    for i in range(5):
        th = threading.Thread(target=DownloadVideoHD, args=(i,))
        th.start()
        logger.info(f"Thread number {i} with DownloadingVideoHD was started.")
    for i in range(5):
        th = threading.Thread(target=DownloadVideoFullHD, args=(i,))
        th.start()
        logger.info(f"Thread number {i} with DownloadingVideoFullHD was started.")
