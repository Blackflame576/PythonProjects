#Libraries
from aiogram import Bot, Dispatcher, executor, types
import sys
import os
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
from pytube import YouTube
import asyncio
from loguru import logger
import sqlite3
from torrentool.api import Torrent
import json
import platform
import time

TOKEN = "5221414424:AAFKCS7TcSfhbkLG3LMmP0BJiVFMzSZ1ako"
VideosForCompress = {}
CompressedVideos = {}
DownloadVideoHD = {}
DownloadVideoFullHD = {}
GetStartedMessage = "👋Hello, I am DownloadYoutubeBot!" +'\n' + "I can download video in resolution HD(720p) and FullHD(1080p)."
GetHelpMessage = "To download the video, just send me the video link 🔗!" + "\n" + "/start - Start Bot" + "\n" + "/help - Call help" + "\n" + "Our support group:https: //t.me/DownloadYoutubeBotSupport"
Commands = {
    "start":["start","start_bot"],
    "stop":["stop","stop bot","stop_bot"],
    "help":["help","help bot","help_bot","help_me","help me","help me please","help please","help_me_please","help_please"],
    "ExampleLinks":["https://youtu.be","https://www.youtube.com","www.youtube.com"]
}
HomeDir = os.path.dirname(os.path.realpath(__file__))
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#Logger
logger.add(HomeDir + '/DownloadYoutubeBot.log',format="{time} {level} {message}",level="DEBUG",rotation="200 MB",diagnose=True)
#Code


#Video in HD resolution
@dp.callback_query_handler(text="HD")
async def HdCompress(call: types.CallbackQuery):
    global VideosForCompress
    global CompressedVideos
    global DownloadVideoHD
    global DownloadVideoFullHD

    if not os.path.exists(HomeDir + '/CompressedVideos.json'):
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/DownloadVideoHD.json'):
        with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(DownloadVideoHD, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    PathVideo = HomeDir + "/DownloadedVideos"
    if os.path.exists(HomeDir + "/Videos"):
        pass
    elif not os.path.exists(HomeDir + "/Videos"):
        os.mkdir(HomeDir + "/Videos")
    video = youtube.streams.filter(res="720p",file_extension='mp4').first()
    if os.path.exists(HomeDir + f'/Videos/{video.default_filename}'):
        download = HomeDir + f'/Videos/{video.default_filename}'
        #Exists PathVideo in list CompressedVideos
        if id_user in CompressedVideos:
            if not download in CompressedVideos[id_user]:
                CompressedVideos[id_user].append(download)
        elif not id_user in CompressedVideos:
            CompressedVideos.update({id_user:[download]})
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    elif not os.path.exists(HomeDir + f'/Videos/{video.default_filename}'):
        await bot.send_message(chat_id = id_user,text = f"Download video '{video.default_filename}'")
        #Exists PathVideo in list VideosForCompress
        if id_user in DownloadVideoHD:
            if not link in DownloadVideoHD[id_user]:
                DownloadVideoHD[id_user].append(link)
        elif not id_user in DownloadVideoHD:
            DownloadVideoHD.update({id_user:[link]})
        with open(HomeDir + "/DownloadVideoHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(DownloadVideoHD, outfile,ensure_ascii=False,sort_keys=True, indent=2)
        await bot.send_message(chat_id = id_user,text = f"Video '{video.default_filename}' was downloaded")
        

#Video in FullHD resolution
@dp.callback_query_handler(text="FullHD")
async def FullHDCompress(call: types.CallbackQuery):
    global VideosForCompress
    global CompressedVideos
    global DownloadVideoHD
    global DownloadVideoFullHD

    if not os.path.exists(HomeDir + '/CompressedVideos.json'):
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/DownloadVideoHD.json'):
        with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(DownloadVideoFullHD, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    PathVideo = HomeDir + "/DownloadedVideos"
    if os.path.exists(HomeDir + "/Videos"):
        pass
    elif not os.path.exists(HomeDir + "/Videos"):
        os.mkdir(HomeDir + "/Videos")
    video = youtube.streams.filter(res="1080p",file_extension='mp4').first()
    if os.path.exists(HomeDir + f'/Videos/{video.default_filename}'):
        download = HomeDir + f'/Videos/{video.default_filename}'
        #Exists PathVideo in list CompressedVideos
        if id_user in CompressedVideos:
            if not download in CompressedVideos[id_user]:
                CompressedVideos[id_user].append(download)
        elif not id_user in CompressedVideos:
            CompressedVideos.update({id_user:[download]})
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    elif not os.path.exists(HomeDir + f'/Videos/{video.default_filename}'):
        await bot.send_message(chat_id = id_user,text = f"Download video '{video.default_filename}'")
        #Exists PathVideo in list VideosForCompress
        if id_user in DownloadVideoFullHD:
            if not link in DownloadVideoFullHD[id_user]:
                DownloadVideoFullHD[id_user].append(link)
        elif not id_user in DownloadVideoFullHD:
            DownloadVideoFullHD.update({id_user:[link]})
        with open(HomeDir + "/DownloadVideoFullHD.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(DownloadVideoFullHD, outfile,ensure_ascii=False,sort_keys=True, indent=2)
        await bot.send_message(chat_id = id_user,text = f"Video '{video.default_filename}' was downloaded")

#Answer to command "/start"
@dp.message_handler(commands=Commands["start"])
async def send_welcome(message: types.Message):
    id_user = message.from_user.id
    await bot.send_message(chat_id = id_user,text = GetStartedMessage)

#Answer to command "/help"
@dp.message_handler(commands=Commands["help"])
async def send_welcome(message: types.Message):
    id_user = message.from_user.id
    await bot.send_message(chat_id = id_user,text = GetHelpMessage)

#Answer to command stop
@dp.message_handler(commands=Commands["stop"])
async def send_welcome(message: types.Message):
    id_user = message.from_user.id
    await bot.send_message(chat_id = id_user,text = "Bot was stopped!")
    logger.info("Bot was stopped!")
    sys.exit()

#Upload video to users
async def UploadVideo():
    global VideosForCompress
    global CompressedVideos

    await asyncio.sleep(1)
    if not os.path.exists(HomeDir + '/CompressedVideos.json'):
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(CompressedVideos, outfile,ensure_ascii=False,sort_keys=True, indent=2)
    if not os.path.exists(HomeDir + '/VideosForCompress.json'):
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump(VideosForCompress,outfile,ensure_ascii=False,sort_keys=True, indent=2)

    try:
        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "r+") as content:
            CompressedVideos = json.load(content)
        i = 0
        for User in CompressedVideos:
            if len(CompressedVideos[User]) >= 1:
                for Video in CompressedVideos[User]:
                    Video = Video
                    User = User
                    if CompressedVideos[User][i]:
                        CompressedVideos[User].remove(Video)
                        with open(HomeDir + "/CompressedVideos.json",encoding='UTF-8',mode = "w+") as outfile:
                            CompressedVideos = json.dump(CompressedVideos,outfile,ensure_ascii=False,sort_keys=True, indent=2)
                        i += 1
                    SizeVideo = (os.stat(Video)).st_size / (1024 * 1024)
                    filename = os.path.basename(Video)#title + ".mp4"
                    if SizeVideo < 50:
                        await bot.send_video(User, open(Video, 'rb'))   
                        logger.info('Video "{}" was sended to user by id {}'.format(filename,User)) 
                    elif SizeVideo > 50:
                        folder_id = '1rr_eep3hcggX3uklfqD6FzhylADPE_Pd'
                        SCOPES = ['https://www.googleapis.com/auth/drive']
                        SERVICE_ACCOUNT_FILE = HomeDir + "/downloadyoutubebot-f30012c75f11.json"
                        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                        service = build('drive', 'v3', credentials=credentials)
                        results = service.files().list(pageSize=10,
                                    fields="nextPageToken, files(id, name, mimeType)").execute()
                        NumberFolder = 0
                        for folder in results['files']:
                            NameFolder = str(results['files'][NumberFolder]["name"])
                            TypeFolder = str(results['files'][NumberFolder]["mimeType"])
                            idFolder = str(results['files'][NumberFolder]["id"])
                            if NameFolder == User and TypeFolder == "application/vnd.google-apps.folder":
                                new_folder_id = idFolder
                            elif NameFolder != User and TypeFolder != "application/vnd.google-apps.folder":
                                folder_metadata = {
                                    "name": [User],
                                    "mimeType": "application/vnd.google-apps.folder",
                                    "parents": [folder_id]
                                }
                                folder = service.files().create(body=folder_metadata, fields="id,webViewLink").execute()
                                new_folder_id = folder.get("id")
                        #print(results['files'][0]["name"])
                        file_metadata = {
                            "name": filename,
                            "mimeType": "video/mpeg",
                            "parents": [new_folder_id]
                        }
                        # upload
                        logger.info("Upload video to Google Drive")
                        await bot.send_message(chat_id=User,text = 'Upload video "{}" to Google Drive'.format((filename).replace(".mp4","")))
                        media = MediaFileUpload(Video, resumable=True)
                        file = service.files().create(body=file_metadata, media_body=media, fields='id,webViewLink').execute()
                        file_permission = {"role": "reader", "type": "anyone"}
                        service.permissions().create(
                            body=file_permission, fileId=file.get("id")
                        ).execute()
                        file_link = file.get("webViewLink")
                        print("File url: {}".format(file.get("webViewLink")))
                        await bot.send_message(chat_id = User,text = "Size of video is high!" + "\n" + "I uploaded video to Google Drive!" + "\n" + "Keep the link: {}".format(file_link))
                        if os.path.exists(HomeDir + '/TorrentFiles'):
                            pass
                        elif not os.path.exists(HomeDir + '/TorrentFiles'):
                            os.mkdir(HomeDir + '/TorrentFiles')
                        TorrentFilePath = HomeDir + '/TorrentFiles' + '/{}.torrent'.format(filename)
                        TorrentFile = Torrent.create_from(Video)  # or it could have been a single file
                        TorrentFile.announce_urls = 'udp://tracker.openbittorrent.com:80'
                        TorrentFile.to_file(TorrentFilePath)
                        logger.info("Created TorrentFile with video '{}'".format(filename))
                        await bot.send_document(User, ('{}.torrent'.format(filename), open(TorrentFilePath, 'rb')))
                    if os.path.exists(Video):
                        if platform.system() == "Windows":
                            os.chmod(Video, 0o777)
                        # os.chmod(Video, os.stat.S_IWRITE)
                        os.remove(Video)
    except FileNotFoundError:
        with open(HomeDir + "/VideosForCompress.json",encoding='UTF-8',mode = "w+") as outfile:
            json.dump({},outfile,ensure_ascii=False,sort_keys=True, indent=2)
        with open(HomeDir + "/CompressedVideos.json", "w+",encoding='UTF-8') as outfile:
            json.dump({}, outfile,ensure_ascii=False,sort_keys=True, indent=2)

#Add user to database
async def AddUser(id,username,first_name,last_name):
    connection = sqlite3.connect(HomeDir + "/users.db")
    database = connection.cursor()
    table = database.execute("""SELECT 'users' FROM sqlite_master WHERE type='table'""").fetchall()
    if table == []:
    	database.execute("CREATE TABLE users (id INTEGER, username TEXT, first_name TEXT, last_name TEXT)")
    elif table != []:
        pass
    data = database.execute("SELECT id, username, first_name, last_name FROM users WHERE id = ?",(id,),).fetchone()
    if data != None:
        pass
    else:
        database.execute("INSERT INTO users (id,username,first_name,last_name)  VALUES  (?,?,?,?)",(id,username,first_name,last_name))
        logger.info("{} was successfully added to database".format(id))
    connection.commit()

#Central system 
@dp.message_handler()
async def GetVideoLink(message: types.Message):
    try:
        global id_user
        id_user = message.from_user.id

        for Command in Commands["ExampleLinks"]:
            if message.text.startswith(Command):
                global title
                global youtube
                global link
                id = message.from_user.id
                username = message.from_user.username
                first_name = message.from_user.first_name
                last_name = message.from_user.last_name
                link = message.text
                youtube = YouTube(link)
                title = youtube.title
                image =youtube.thumbnail_url
                author = youtube.author
                length = round(youtube.length / 60)
                HD = youtube.streams.filter(res="720p",file_extension='mp4').first()
                FullHD = youtube.streams.filter(res="1080p",file_extension='mp4').first()
                keyboard = types.InlineKeyboardMarkup()
                if HD != None:
                    keyboard.add(types.InlineKeyboardButton(text="HD(720p) with compress", callback_data="HD"))
                if FullHD != None:
                    keyboard.add(types.InlineKeyboardButton(text="FullHD(1080p) with compress", callback_data="FullHD"))
                await bot.send_photo(chat_id = id_user,photo = image,caption = 'ℹName video - {}'.format(title) + '\n' + f'Length video - {length}' + '\n' + f'Author video - {author}',reply_markup = keyboard)
                asyncio.create_task(AddUser(id,username,first_name,last_name))
    except NameError as error:
        logger.error(error)

def StartUploadVideo():
    asyncio.run(UploadVideo())

def Start():
    logger.info("Bot was started!")
    logger.info("Listening messages!")

#Run code
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=Start())